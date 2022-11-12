import ArkesUtility as AU
import ArkesInstance as AI

# Start the Arkes Instance
ExchangeAccount = AI.ExchangeAccountSetup()
ExchangeAwaitingFolder, ExchangeSuccessfulFolder, ExchangeFailedFolder = AI.ExchangeFolderConfig(ExchangeAccount)
AI.ExchangeEmailProcessing(ExchangeAwaitingFolder, ExchangeSuccessfulFolder, ExchangeFailedFolder)