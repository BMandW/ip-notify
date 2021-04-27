#!/bin/bash

(
    cd golang;
    GOOS=linux GOARCH=amd64 go build -o ../dist/ip-finder-go .;
    GOOS=windows GOARCH=amd64 go build -o ../dist/ip-finder-go.exe .;
    GOOS=darwin GOARCH=amd64 go build -o ../dist/ip-finder-go-mac .;
)
