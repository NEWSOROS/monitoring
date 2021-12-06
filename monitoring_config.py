from common import ValidatorConfig

config = ValidatorConfig(
    validator_name="TEST1",
    secrets_path="/home/sol",
    local_rpc_address="http://localhost:8899",
    remote_rpc_address="http://api.testnet.solana.com",
    cluster_environment="testnet",
    debug_mode=False
)
