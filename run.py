import os

from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

date = "31 de diciembre de 2021"

def getNum(index, name):
    index = index + 0
    if index < 10:
        return "I00{} - ".format(index) + name
    if index > 9 and index < 99:
        return "I0{} - ".format(index) + name
    return name


def delete_old_data():
    for i in os.listdir("generated-certificates/"):
        os.remove("generated-certificates/{}".format(i))


def generate_certificates():

    #    for index, name in enumerate(list_of_names):
    #       certificate_template_image = cv2.imread("certificate-template.jpg")
    #       cv2.putText(certificate_template_image, name.strip(), (390,290), cv2.FONT_HERSHEY_SIMPLEX, 1, (250, 250, 250), 1, cv2.LINE_AA)
    #       cv2.imwrite("generated-certificates/{}.jpg".format(name.strip()), certificate_template_image)
    #       print(name.strip())
    #       print("Processing {} / {}".format(index + 1,len(list_of_names)))

    df = pd.read_csv('people.csv')
    fontName = ImageFont.truetype('libre.ttf', 55)

    for index, j in df.iterrows():
        print("Processing {} / {}".format(index + 1, len(df)))



        img = Image.open('certificate-template.jpg')
        draw = ImageDraw.Draw(img)
        draw.text(xy=(750, 600), text='{}'.format(
            j['name']), fill=(0, 0, 0), font=fontName, anchor="mm", align="center")
        
        img.save(
            'generated-certificates/{}.jpg'.format(getNum(index, j['name'])))


def main():
    delete_old_data()
    generate_certificates()


if __name__ == '__main__':
    main()
