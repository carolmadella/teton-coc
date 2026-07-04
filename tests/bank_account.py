# bank_account.py

def create_account(name, opening_balance=0):
    """
    Return a new account represented as a dict:
      {"name": name, "balance": int, "transactions": list}
    If opening_balance != 0, record ("opening_balance", opening_balance).
    Notice this is a TUPLE () rather than a LIST []. 
    A tuple is just an immutable version of a list.
    """
    # TODO: validate name and opening_balance when appropriate
    acct = {
        "name": name,
        # store integer balance
        "balance": 0,
        # transaction list
        "transactions": [],
    }
    if opening_balance != 0:
        acct["balance"] = opening_balance
        acct["transactions"].append(("opening_balance", opening_balance))
    return acct

def deposit(account, amount):
    """
    Add amount to account["balance"] and record ("deposit", amount).
    - amount must be a positive integer; otherwise raise ValueError.
    - modify account in-place and return True.
    """
    # Check that deposit amount is a positive number
    if amount <= 0:
        raise ValueError("Deposit amount must be greater than zero")

    # Add the deposit amount to the current balance
    account["balance"] += amount

    # Add the deposit to the transaction list
    account["transactions"].append(("deposit", amount))

    # Return True to indicate success
    return True

def withdraw(account, amount):
    """
    Subtract amount from account["balance"] and record ("withdraw", amount).
    - amount must be a positive integer and <= balance; otherwise raise ValueError.
    - modify account in-place and return True.
    """
    # Check if the withdraw amount is positive and does not exceed the current balance
    if amount <= 0 or amount > account["balance"]:
        raise ValueError("Invalid withdraw amount or insufficient funds")

    # Subtract the withdraw amount from the current balance
    account["balance"] -= amount

    # Add the withdraw to the transaction list
    account["transactions"].append(("withdraw", amount))

    # Return True to indicate success
    return True

def transfer(from_account, to_account, amount):
    """
    Transfer amount from from_account to to_account.
    - both accounts must be valid account dicts (created by create_account)
    - amount must be positive integer and <= from_account balance
    - on success: mutate both accounts, record ("transfer_out", amount)
      in from_account and ("transfer_in", amount) in to_account, then return True.
    - on failure: raise ValueError without mutating accounts.
    """
    # Check that both accounts are valid dictionaries with the required keys
    if (not isinstance(from_account, dict) or not isinstance(to_account, dict) or
        "name" not in from_account or "name" not in to_account or
        "balance" not in from_account or "balance" not in to_account or
        "transactions" not in from_account or "transactions" not in to_account):
        raise ValueError("One or both accounts are invalid")
    
    # Validate that the amount is positive and doesn't exceed the current balance
    if amount <= 0 or amount > from_account["balance"]:
        raise ValueError("Invalid transfer amount or insufficient funds")

    # Deduct the amount from the sender and add it to the recipient
    from_account["balance"] -= amount
    to_account["balance"] += amount

    # Record the transactions in both from and to account transaction lists
    from_account["transactions"].append(("transfer_out", amount))
    to_account["transactions"].append(("transfer_in", amount))
        
    # Return True to indicate success
    return True

def account_str(account):
    """
    Return a readable single-line summary like "Alice: 100"
    """
    # Format and return a string in the style of "Name: Balance"
    return f"{account['name']}: {account['balance']}"
