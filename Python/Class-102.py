import cv2
import random
import time
import dropbox

start_time = time.time()
def take_pic():
    num = random.randint(0, 100)
    video = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = video.read()
        img_name = "img" + str(num) + ".jpg"
        cv2.imwrite(img_name, frame)
        result = False

    return img_name
    print("Picture taken.")
    video.release()
    cv2.destroyAllWindows()

def uploadFile(img_name):
    accessToken = "sl.A-RaYepXAFIBs46P8GZ-fG_lPXkCnYfGGa9VsHuVXDjZ4KWO-6OyFGew-KhmoWhRYVFyki_9DSbQgg25woE4gQnLZlImqSLpJ0OlPRX_5dkg5i7y1BU47ItyMfU33EyfOHeyoAoiUI3_"
    fileFrom = img_name
    fileTo = "/PythonPics/" + img_name
    dbx = dropbox.Dropbox(accessToken)

    with open(fileFrom, "rb") as f:
        dbx.files_upload(f.read(), fileTo, mode = dropbox.files.WriteMode.overwrite)
        print("File uploaded.")

def main():
    while(True):
        if((time.time() - start_time) >= 20):
            name = take_pic()
            uploadFile(name)

main()

