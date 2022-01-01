import os

from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os


def getNum(index,name):
   if index < 10:
      return "P00{} - ".format(index) + name
   if index > 9 and index < 99:
      return "P0{} - ".format(index) + name
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

    df = pd.read_csv('final-names.csv')
    font = ImageFont.truetype('google.ttf', 80)
    for index, j in df.iterrows():
        print("Processing {} / {}".format(index + 1, len(df)))
        img = Image.open('certificate-template.jpg')
        draw = ImageDraw.Draw(img)
        draw.text(xy=(792,570),text='{}'.format(j['name']),fill=(255,255,255),font=font, anchor="mm")
        img.save('pictures/{}.jpg'.format(getNum(index,j['name'])))
      


def main():
   delete_old_data()
   generate_certificates()



if __name__ == '__main__':
   main()
