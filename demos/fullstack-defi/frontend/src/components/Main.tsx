import { useEthers } from "@usedapp/core"
import helperConfig from "../helper-config.json"
import networkMapping from "../chain-info/deployments/map.json"
import { constants } from "ethers"
import brownieConfig from "../brownie-config.json"
import dapp from "../dapp.png"
import fau from "../dai.png"
import eth from "../eth.png"
import { YourWallet } from "./yourWallet/YourWallet"

export type Token = {
  image: string
  address: string
  name: string
}

export const Main = () => {
  // show token values from the wallet
  // get the address of different tokens
  // get the balance of the users wallet
  // send the brownie-config to our 'src' folder
  // send the build folder
  const { chainId } = useEthers()
  const networkName = chainId ? helperConfig[chainId] : "dev"
  const dappTokenAddress = chainId ? networkMapping[String(chainId)]["dappToken"][0] : constants.AddressZero
  const wethTokenAddress = chainId ? brownieConfig["networks"][networkName]["weth_token"] : constants.AddressZero
  const fauTokenAddress = chainId ? brownieConfig["networks"][networkName]["fau+token"] : constants.AddressZero

  const supportedTokens: Array<Token> = [
    {
      image: dapp,
      address: dappTokenAddress,
      name: "DAPP"
    },
    {
      image: eth,
      address: wethTokenAddress,
      name: "WETH"
    },
    {
      image: fau,
      address: fauTokenAddress,
      name: "DAI"
    }
  ]
  return (<YourWallet supportedTokens={supportedTokens} />)
};
