build:
	docker-compose -p streamlit-strava -f docker/docker-compose.yml build

serve:
	docker-compose -f docker/docker-compose.yml --env-file ./.env.local up

publish_cloud_run: export VERSION=0.1.0

publish_cloud_run:
	gcloud config configurations activate gssns
	docker tag streamlit-strava:latest gcr.io/generic-310412/streamlit-strava:latest
	docker push gcr.io/generic-310412/streamlit-strava:latest
	docker tag streamlit-strava:latest gcr.io/generic-310412/streamlit-strava:${VERSION}
	docker push gcr.io/generic-310412/streamlit-strava:${VERSION}
	gcloud run deploy streamlit-strava --platform managed --allow-unauthenticated --image gcr.io/generic-310412/streamlit-strava:${VERSION}
