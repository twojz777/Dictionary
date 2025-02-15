data = [
    ("Cryptocurrency", "Digital currency using cryptography for security."),
    ("Blockchain", "A decentralized digital ledger for transactions."),
    ("Bitcoin", "The first and most popular cryptocurrency."),
    ("Altcoin", "Any cryptocurrency other than Bitcoin."),
    ("Ethereum", "A blockchain enabling smart contracts and DApps."),
    ("Smart Contract", "Self-executing agreements on blockchain."),
    ("Decentralization", "No central authority controls the system."),
    ("Mining", "Process of validating transactions and earning coins."),
    ("Proof of Work", "A mining-based consensus mechanism."),
    ("Proof of Stake", "A staking-based consensus mechanism"),
    ("Token", "Digital assets created on a blockchain."),
    ("Stablecoin", "Crypto pegged to stable assets like USD."),
    ("DeFi", "Financial services without intermediaries."),
    ("NFT", "Unique digital ownership certificates."),
    ("Gas Fee", "Transaction fees on blockchain networks."),
    ("Fork", "A split in a blockchain network."),
    ("Metaverse", "A virtual world using blockchain and NFTs."),
    ("Oracles", "Services bringing real-world data to smart contracts."),
    ("Private Key", "A secret code to access a wallet."),
    ("Public Key", "A wallet address for receiving funds."),
    ("Cold Wallet", "Offline storage for better security."),
    ("Hot Wallet", "Online storage for easy access."),
    ("Exchange", "A platform for buying and selling crypto."),
    ("Liquidity", "How easily an asset is traded."),
    ("Market Cap", "Total value of a cryptocurrency."),
    ("HODL", "Holding crypto long-term despite volatility."),
    ("Rug Pull", "A scam where developers steal investor funds."),
    ("ByBit", "A cryptocurrency derivatives trading platform.."),
    ("Phantom Wallet", "A Solana-based crypto wallet for DeFi and NFTs."),
    ("Binance", "The world’s largest cryptocurrency exchange."),
]

def get_definition(term):
    for t, definition in data:
        if t==term:
            return definition
    return "Term not found."

print("Data")
print("Available terms:", [t for t, _ in data])

user_input=input("Enter a term to get its definition:")
print("Definition:",get_definition(user_input))