import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/feed"  # Local FastAPI endpoint

def get_recommendations(username):
    try:
        response = requests.get(API_URL, params={"username": username})
        data = response.json()
        if "videos" in data:
            recs = "\n".join(data["videos"])
            return f"Recommended videos for {username}:\n{recs}"
        else:
            return f"No videos found for {username}"
    except Exception as e:
        return f"Error fetching recommendations: {e}"

demo = gr.Interface(
    fn=get_recommendations,
    inputs=gr.Textbox(label="Enter username"),
    outputs=gr.Textbox(label="Recommendations"),
    title="Video Recommendation Engine",
    description="Enter a username to get personalized video recommendations"
)

if __name__ == "__main__":
    demo.launch()
