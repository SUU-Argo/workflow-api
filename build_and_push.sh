#!/usr/bin/env bash

# Define variables
DOCKER_USERNAME="suuargo"
IMAGE_NAME="workflow-api"
TAG="0.0.3"

set -e

echo "Logging in to Docker Hub..."
docker login

# Build the Docker image
echo "Building Docker image..."
docker build -t ${IMAGE_NAME} --platform="linux/amd64" .

# Tag the image for Docker Hub
echo "Tagging Docker image..."
docker tag ${IMAGE_NAME} ${DOCKER_USERNAME}/${IMAGE_NAME}:${TAG}

# Push the image to Docker Hub
echo "Pushing Docker image to Docker Hub..."
docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:${TAG}

echo "Docker image pushed successfully!"