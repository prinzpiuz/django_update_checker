<h1 align="center" id="heading">Django Update Checker</h1>
<p align="center">
<a href="https://www.gnu.org/licenses/gpl-3.0" alt="License: GPLv3"><img src="https://img.shields.io/badge/License-GPL%20v3-blue.svg"></a>
<img src="https://img.shields.io/github/forks/prinzpiuz/django_update_checker">
</p>

This is small script for checking any new updates/bugfixes/security fixes released in django [News & Events](https://www.djangoproject.com/weblog/) and sending corresponding notifications in MS teams configured channel, without any deployments or server hosting, we are using [Scheduled events](https://docs.github.com/en/actions/learn-github-actions/events-that-trigger-workflows#scheduled-events) in github actions for this. this is similar to cron jobs in unix systems

##### Screenshot

[<img src="team_screenshot.png">](team_screenshot.png)

##### How to use

- Fork this repo
- Go to actions page and enable actions on forked repo (it will be disabled by default in forked repo)
- Get an incomming Teams webhook url. for reference, please check [Teams  Incomming Webhook URL ](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)
- Add webhook URL as MS_TEAMS_WEBHOOK_URI in your cloned repos Settings --> Secrets. for reference, please check [GitHub Secrets ](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository)

##### Run Locally

Clone the project

```bash
  git clone git@github.com:prinzpiuz/django_update_checker.git
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python checker.py --url <teams webhook url>
```