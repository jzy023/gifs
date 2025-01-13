from moviepy import VideoFileClip, clips_array


def crop_vid(input_path):

    x1 = 800
    y1 = 300
    x2 = 1400
    y2 = 1500

    # Load the video
    video = VideoFileClip(input_path)
    video = video.cropped(x1, y1, x2, y2)

    return video 



def concatenation_vids(input_path_list, output_path):
    videos = []
    for path in input_path_list:
        video = crop_vid(path)
        videos.append(video)

    concatenated_video = clips_array([videos])
    concatenated_video.write_videofile(output_path, codec="libx264", audio_codec="aac")




if __name__ == "__main__":
    # Path to the input video
    input_video_path = "bubble.mp4"
    input_video_path_list = [
                             "bubble_lowST.mp4"
                            ,"bubble.mp4"
                            ,"bubble_hiST.mp4"
                            ]

    # Path to the output video
    output_video_path = "output_video.mp4"

    # Call the function
    concatenation_vids(input_video_path_list, output_video_path)
