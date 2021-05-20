build:
	docker-compose -p streamlit-activity-viewer -f docker/docker-compose.yml build

serve:
	docker-compose -f docker/docker-compose.yml --env-file ./.env.local up

publish_cloud_run: export VERSION=0.5.1

publish_cloud_run:
	gcloud config configurations activate gssns
	docker tag streamlit-activity-viewer:latest gcr.io/generic-310412/streamlit-activity-viewer:latest
	docker push gcr.io/generic-310412/streamlit-activity-viewer:latest
	docker tag streamlit-activity-viewer:latest gcr.io/generic-310412/streamlit-activity-viewer:${VERSION}
	docker push gcr.io/generic-310412/streamlit-activity-viewer:${VERSION}
	gcloud run deploy streamlit-activity-viewer --platform managed --allow-unauthenticated --image gcr.io/generic-310412/streamlit-activity-viewer:${VERSION}
