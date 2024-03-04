
def check(m, music):
    return m in music

def get_music(info):
    exc = {'C#' :'1' ,'D#' :'2', 'F#' :'3', 'G#' :'4', 'A#' :'5', "B#": '6'}
    for k, v in exc.items():
        info = info.replace(k, v)
    return info

def get_music_info(info, music_time):
    result = get_music(info)
    if music_time >= len(result):
        return result * (music_time // len(result)) + result[:music_time %len(result)]
    else:
        return result[:music_time]

def get_time(t):
    return int(t.split(':')[0] ) *60 + int(t.split(':')[1])


def get_musicinfo(m, musicinfo):
    start, end, title, info = musicinfo.split(",")
    music_time = get_time(end) - get_time(start)
    music = get_music_info(info, music_time)
    return [music_time, check(get_music(m), music), title]

def solution(m, musicinfos):
    answer = ["", 0]
    for musicinfo in musicinfos:
        result = get_musicinfo(m, musicinfo)
        if result[1] and result[0] > answer[1]:
            answer = [result[2], result[0]]
    if not answer[0]:
        return "(None)"
    return answer[0]