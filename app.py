from flask import *
import youtube_dl

app = Flask(__name__)

def get_video_information(url, search_type):
    ll = [{'video_response': [], 'video_info': []}]
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    with ydl:
        result = ydl.extract_info(url, download=False)
    if 'entries' in result:
        video = result['entries'][0]
    else:
        video = result

    for i in video['formats']:
        if search_type == 'MP4':
            if i['ext'] == 'mp4':
                for index, value in enumerate(ll):
                    value['video_response'].append(i)
            if i['ext'] == 'm4a':
                for index, value in enumerate(ll):
                    value['video_response'].append(i)
        elif search_type == 'ALL':
            for index, value in enumerate(ll):
                value['video_response'].append(i)
        else:
            for index, value in enumerate(ll):
                value['video_response'].append(i)

    video_title = video['title']
    video_images = video['thumbnails']
    for index, value in enumerate(ll):
        new_json_row = {
            'title': video_title,
            'thumbnails': video_images
        }
        value['video_info'].append(new_json_row)
    return jsonify(ll)


@app.route('/get_video')
def get_video():
    video_id = request.args.get('id')
    search_type = request.args.get('stype')
    if video_id:
        if search_type == 'MP4':
            video_url = 'https://www.youtube.com/watch?v={}'.format(video_id)
            return get_video_information(video_url, search_type)
        elif search_type == 'ALL':
            video_url = 'https://www.youtube.com/watch?v={}'.format(video_id)
            return get_video_information(video_url, search_type)
        else:
            video_url = 'https://www.youtube.com/watch?v={}'.format(video_id)
            return get_video_information(video_url, '')
    else:
        return jsonify({
            'msg': 'video id parameter is require'
        }), 404


@app.route('/')
def hello_world():
    return 'Welcome to youtube-dl API'


if __name__ == '__main__':
    app.run()
