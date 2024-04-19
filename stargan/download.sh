FILE=$1

if [ $FILE == "celeba" ]; then

    # CelebA images and attribute labels
    URL=https://drive.google.com/uc?id=0B7EVK8r0v71pZjFTYXZWM3FlRnM
    ZIP_FILE=./data/celeba.zip
    mkdir -p ./data/
    gdown $URL -O $ZIP_FILE
    unzip $ZIP_FILE -d ./data/
    rm $ZIP_FILE


elif [ $FILE == 'pretrained-celeba-128x128' ]; then

    # StarGAN trained on CelebA (Black_Hair, Blond_Hair, Brown_Hair, Male, Young), 128x128 resolution
    URL=https://www.dropbox.com/s/7e966qq0nlxwte4/celeba-128x128-5attrs.zip?dl=0
    ZIP_FILE=./stargan_celeba_128/models/celeba-128x128-5attrs.zip
    mkdir -p ./stargan_celeba_128/models/
    wget -N $URL -O $ZIP_FILE
    unzip $ZIP_FILE -d ./stargan_celeba_128/models/
    rm $ZIP_FILE

elif [ $FILE == 'pretrained-celeba-256x256' ]; then

    # StarGAN trained on CelebA (Black_Hair, Blond_Hair, Brown_Hair, Male, Young), 256x256 resolution
    URL=https://www.dropbox.com/s/zdq6roqf63m0v5f/celeba-256x256-5attrs.zip?dl=0
    ZIP_FILE=./stargan_celeba_256/models/celeba-256x256-5attrs.zip
    mkdir -p ./stargan_celeba_256/models/
    wget -N $URL -O $ZIP_FILE
    unzip $ZIP_FILE -d ./stargan_celeba_256/models/
    rm $ZIP_FILE

else
    echo "Available arguments are celeba, pretrained-celeba-128x128, pretrained-celeba-256x256."
    exit 1
fi