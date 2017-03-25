# build containers
cd containers
cd data_layer
bash ./gen_word_data.sh
docker build -t sendmarsh/wordtools_data .
cd ../api_layer
docker build -t sendmarsh/wordtools_api .
cd ../presentation_layer
docker build -t sendmarsh/wordtools_presentation .
cd ../..