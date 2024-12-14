from flask import Flask, jsonify

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

def merge_sort_videos(video_titles):
    if len(video_titles) <= 1:
        return video_titles 

    mid = len(video_titles) // 2
    left_half = merge_sort_videos(video_titles[:mid])
    right_half = merge_sort_videos(video_titles[mid:])

    return merge_alphabetical(left_half, right_half)

def merge_alphabetical(left, right):
    sorted_videos = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:  
            sorted_videos.append(left[i])
            i += 1
        else:
            sorted_videos.append(right[j])
            j += 1

    sorted_videos.extend(left[i:])
    sorted_videos.extend(right[j:])
    return sorted_videos

@app.route('/videos/sorted', methods=['GET'])
def get_sorted_videos():
    sorted_videos = merge_sort_videos(video_titles)
    return jsonify({"sorted_videos": sorted_videos}), 200

if __name__ == '__main__':
    app.run(debug=True)
