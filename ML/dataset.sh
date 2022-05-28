echo "Make Sure you have your kaggle.json file..." 
echo "Starting to install packages and Datasets..." 
pip install kaggle
mkdir ~/.kaggle
cp kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
kaggle datasets download -d adityajn105/flickr8k
unzip flickr8k.zip 