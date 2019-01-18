# build containers
cd containers
cd data_layer
bash ./gen_word_data.sh
docker build -t sendmarsh/wordtools-data .
docker push sendmarsh/wordtools-data
cd ../api_layer
touch api_layer.py
docker build -t sendmarsh/wordtools_api .
docker push sendmarsh/wordtools-api
cd ../presentation_layer
docker build --no-cache -t sendmarsh/wordtools-presentation .
docker push sendmarsh/wordtools-presentation
cd ../..

