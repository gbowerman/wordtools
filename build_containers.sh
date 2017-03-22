# build containers
cd containers
cd data_layer
bash ./gen_word_data.sh
docker build -t wordtools_data .
cd ../api_layer
docker build -t wordtools_api .
cd ../presentation_layer
docker build -t wordtools_presentation .
cd ../..