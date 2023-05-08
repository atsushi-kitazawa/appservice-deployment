param webAppName string = ''
param sku string = ''
param linuxFxVersion string = ''
param repositoryUrl string = ''
param branch string = ''
param location string = resourceGroup().location
param clientId string
param tenantId string
var appServicePlanName = toLower('AppServicePlan-${webAppName}')
var webSiteName = toLower('wapp-${webAppName}')
resource appServicePlan 'Microsoft.Web/serverfarms@2020-06-01' = {
  name: appServicePlanName
  location: location
  properties: {
    reserved: true
  }
  sku: {
    name: sku
  }
  kind: 'linux'
}
resource appService 'Microsoft.Web/sites@2020-06-01' = {
  name: webSiteName
  location: location
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      linuxFxVersion: linuxFxVersion
    }
  }
}
resource srcControls 'Microsoft.Web/sites/sourcecontrols@2021-01-01' = {
  name: '${appService.name}/web'
  properties: {
    repoUrl: repositoryUrl
    branch: branch
    isManualIntegration: true
  }
}
resource authSettings 'Microsoft.Web/sites/config@2021-02-01' = {
  name: '${webAppName}/authsettings'
  properties: {
    enabled: true
    unauthenticatedClientAction: 'RedirectToLoginPage'
    defaultProvider: 'AzureActiveDirectory'
    clientId: clientId
    issuer: 'https://sts.windows.net/${tenantId}/'
    allowedAudiences: [
      'https://${webAppName}.azurewebsites.net'
    ]
    additionalLoginParams: [
      {
        name: 'resource'
        value: 'https://graph.microsoft.com'
      }
    ]
  }
}
