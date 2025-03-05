class AccountPageLocators:
    DEPOSIT_BTN = "//button[@ng-class='btnClass2']"
    WITHDRAW_BTN = "//button[@ng-class='btnClass3']"
    TRANSACTIONS_BTN = "button:has-text('Transactions')"
    AMOUNT_INPUT = "input[type='number']"
    SUBMIT_BTN = "button[type='submit']"
    BALANCE = "body > div.ng-scope > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)"
    ACCOUNT_SELECT = "#accountSelect"
    TRANSACTIONS_MSG = ("body > div.ng-scope > div > div.ng-scope > div > "
                        "div.container-fluid.mainBox.ng-scope > div > span")
    MSG = "body > div.ng-scope > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > span"
    ACCOUNT_ID = "body > div.ng-scope > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(1)"
    HOME_BTN = "button[class='btn home']"
