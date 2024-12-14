from flask import Flask, request, jsonify

app = Flask(__name__)


video_titles = [
    "Artificial Intelligence Revolution",
    "Cooking Masterclass: Italian Cuisine",
    "Digital Photography Essentials",
    "Exploring the Cosmos",
    "Financial Planning for Beginners",
    "Fitness Fundamentals: Strength Training",
    "History Uncovered: Ancient Civilizations",
    "Nature's Wonders: National Geographic",
    "The Art of Coding",
    "Travel Diaries: Discovering Europe"
]

# Binary Search 
def binary_search(sorted_list, target):
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# GET method used with Postman
@app.route('/search', methods=['GET'])
def search_video():
    query = request.args.get('title')
    if not query:
        return jsonify({"error": "Title query parameter is required"}), 400

    index = binary_search(video_titles, query)
    if index != -1:
        return jsonify({"message": "Video found", "title": video_titles[index]}), 200
    else:
        return jsonify({"message": "Video not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
