
import sqlite3


class Databaser:

    def __init__(self, db_name='database.db'):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS videos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            name TEXT,
                            desc TEXT,
                            likes INT,
                            dislikes INT,
                            author_name TEXT)''')

    def add_video(self, name, desc, author_name):
        self.cursor.execute('''INSERT INTO videos (name, desc, likes, dislikes, author_name) 
        VALUES (?, ?, 0, 0, ?)''', (name, desc, author_name))
        self.connection.commit()

    def get_video(self, video_id):
        self.cursor.execute('SELECT * FROM videos WHERE id = ?', (video_id,))
        r = self.cursor.fetchone()

        if not r:
            return

        return dict(r)

    def change_video(self, video_id, name=None, desc=None, author_name=None):
        old = self.get_video(video_id)

        if name is None:
            name = old['name']
        if desc is None:
            desc = old['desc']
        if author_name is None:
            author_name = old['author_name']

        self.cursor.execute('UPDATE videos SET name = ?, desc = ?, author_name = ? WHERE id = ?', (name, desc, author_name, video_id))
        self.connection.commit()

    def like_video(self, video_id):
        self.cursor.execute('UPDATE videos SET likes = likes + 1 WHERE id =?', (video_id,))

    def dislike_video(self, video_id):
        self.cursor.execute('UPDATE videos SET dislikes = dislikes + 1 WHERE id =?', (video_id,))

    def get_videos(self):
        self.cursor.execute('SELECT * FROM videos')
        videos = self.cursor.fetchall()

        videos = list(map(dict, videos))
        videos.sort(key=lambda x: x['likes'] - x['dislikes'], reverse=True)

        return videos


if __name__ == '__main__':
    db = Databaser()
    db.add_video('Axwell Ingrosso - More Than You Know', '730 млн просмотров 7 лет назад', 'Axwell Ingrosso')
    db.add_video('Major Lazer & DJ Snake - Lean On (feat. MØ) [Official 4K Music Video]', '3 762 272 813 просмотров 10 лет назад', 'Major Lazer Official')
    db.add_video('Fifth Harmony - Worth It (Official Video) ft. Kid Ink', '2 349 169 043 просмотров 10 лет назад', 'Fifth Harmony')
    db.add_video('Tiësto, Jonas Blue & Rita Ora - Ritual (Official Video)', '218 млн просмотров 5 лет назад', 'Tiësto')
    db.add_video('Olivia Rodrigo - good 4 u (Official Video)', '508 млн просмотров 3 лет назад', 'Olivia Rodrigo')
    db.add_video('Mabel - Mad Love (Official Video)', '133 млн просмотров 5 лет назад', 'Mabel ')
    db.add_video('Tiësto - Lay Low (Official Music Video)', '66 млн просмотров 2 лет назад', 'Tiësto ')
    db.add_video('Zerb & The Chainsmokers - Addicted ft. Ink (Official Video)', '11 млн просмотров 1 год назад', 'The Chainsmokers ')
    db.add_video('P!nk - Just Like Fire (From"Alice Through The Looking Glass" - Official Video)', '294 млн просмотров 8 лет назад', 'P!NK ')
    db.add_video('Jonas Brothes ft. KAROL G - X (Official Music Video)', '47 млн просмотров 4 года назад', 'Jonas Brothes ')
    db.add_video('DJ Snake - Taki Taki ft. Selena Gomez, Ozuna, Cardi B (Official Music Video)', '2 676 796 747 просмотров 6 лет назад', 'DJ Snake ')
    db.add_video('''Justin Timberlake - CAN'T STOP THE FEELING! (from DreamWorks Animation's "TROLLS") (Official Video)''', '1 856 486 409 просмотров 8 лет назад', 'Justin Timberlake ')
    db.add_video('Rita Ora - Let You Love Me [Official Video]', '570 млн просмотров 6 лет назад', 'Rita Ora')
    db.add_video('Jonas Blue - Wild ft. Chelcee Grimes, TINI, Jhay Cortez (Official Video)', '70 млн просмотров 6 лет назад', 'Jonas Blue ')
    db.add_video('DNCE - Cake By The Ocean', '540 млн просмотров 9 лет назад', 'DNCE ')
    db.add_video('LITTLE BIG – FARADENZA (official music video)', '460 млн просмотров 6 лет назад', 'Little Big ')
    db.add_video('Fifth Harmony - Work from Home (Official Video) ft. Ty Dolla $ign', '2 959 434 421 просмотров 9 лет назад', 'Fifth Harmony ')
    db.add_video('Zerb - Mwaki (Feat. @Sofiya_Nzau) [Official Music Video]', '39 млн просмотров 1 год назад', 'Zerb ')
    db.add_video('Jonas Brothers - What A Man Gotta Do (Official Video)', '132 млн просмотров 5 лет назад', 'Jonas Brothers ')
    db.add_video('''David Guetta & Chris Willis Feat. Fergie & LMFAO - Gettin' Over You (Official Video)''', '288 млн просмотров 14 лет назад', 'David Guetta ')

