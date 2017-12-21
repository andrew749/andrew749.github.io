# My Personal Website

Master is the live code for my website.

These instructions are mostly for me to remember the deploy procedure but feel free to take a look.

## Install dependencies

```
yarn install
```

```
pip install -r requirements.txt
```

## Development
```
yarn build-dev
```


## Deploy
First you need to build your css and js sources and then:

```
gcloud app deploy app.yaml
```
