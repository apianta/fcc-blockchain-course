import { useEthers } from "@usedapp/core"
import helperConfig from "../helper-config.json"

export const Main = () => {
  // show token values from the wallet
  // get the address of different tokens
  // get the balance of the users wallet
  // send the brownie-config to our 'src' folder
  // send the build folder
  const { chainId } = useEthers()
  const networkName = chainId ? helperConfig[chainId] : "dev"
  console.log(chainId)
  console.log(networkName)
  // const dappTokenAddress

};
