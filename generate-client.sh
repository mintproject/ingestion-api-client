dir=${PWD}
parentdir="$(dirname "$dir")"

docker run -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v4.1.2 \
     generate  \
     -i /local/openapi.yaml \
     -g python  \
     -o /local/ \
     -c /local/openapi-config.json \
     --template-dir /local/.openapi-generator/template
