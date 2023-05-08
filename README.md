# appservice-deployment

# memo
* アプリ登録だけではエンタープライズアプリケーションには登録されない。サービスプリンシパルの作成をあわせて行う必要がありそう。
* アプリについても以下の点の修正が必要そう。
  * リダイレクトURLをAppServiceのURLにあわせる
  * 承認エンドポイントによって発行してほしいトークンのところを「IDトークン」にする
  * サポートされるアカウントの種類を「この組織ディレクトリのみ」にする
# 参考URL

* GitHub Actionsでリソースをデプロイする
  * [Deploy Bicep files by using GitHub Actions - Azure Resource Manager | Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-github-actions?tabs=userlevel%2CCLI)
* ARMでデプロイするGitHub Actions
  * [Azure/arm-deploy: ARM action to deploy an Azure Resource Manager (ARM) template to all the deployment scopes](https://github.com/Azure/arm-deploy)
* リポジトリを作成するGitHubのREST API
  * [Repositories - GitHub Docs](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#create-an-organization-repository)
* GitHub Actionsの手動実行でパラメータを指定する方法
  * [Set runtime parameters to your GitHub Actions workflows Damien Aicheh](https://damienaicheh.github.io/github/actions/2022/01/20/set-dynamic-parameters-github-workflows-en.html)
* AppService認証のBicep
  * [Microsoft.Web/sites/config 'authsettingsV2' - Bicep, ARM template & Terraform AzAPI reference | Microsoft Learn](https://learn.microsoft.com/en-us/azure/templates/microsoft.web/sites/config-authsettingsv2?pivots=deployment-language-bicep#globalvalidation)