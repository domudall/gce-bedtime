# gce-bedtime
Put `turnoffall` and `turnonall` into cron with appropriate schedule configs.

These environment variables need to be specified:
- `GCP_PROJECT_ID` - project ID (name, not numeric)
- `GCP_ZONE` - compute zone such as europe-west1-d

If you wish to add Slack notifications for on/off actions, you'll need to specify another environment variable:

- `SLACK_TOKEN` - Slack token for authenticating with the incoming web hook integration
