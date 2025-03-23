Given a list of accounts where each element is an entry in a map, where the key is an ID, and the value is a list of emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same group of IDs of the same person if there is some common email to both accounts. A person can have any number of IDs.
After merging the accounts, return the accounts in the following format: the elements of each account are all of the IDs of the same person. The account themselves can be returned in any order.

Input accounts =

  {
    "C1": ["a", "b"], "C2": ["c"],
    "C3": ["b", "d"], "C4": ["d"],
    "C5": ["e"], "C6": ["c"], "C7": ["a"]
  }

Output = [[C1, C3, C4, C7], [C2, C6], [C5]]
