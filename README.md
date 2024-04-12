# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).
```
tokenB tokenA 5.655321988655322
tokenA tokenD 2.4587813170979333
tokenD tokenC 5.0889272933015155
tokenC tokenB 20.129888944077443
tokenB->tokenA->tokenD->tokenC->tokenB, tokenB balance=20.129888944077443.
```
## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

```
Uniswap V2通過在執行交易前將交易數量限制在一定範圍內來解決滑點問題。這是通過swapExactTokensForTokens函數實現的。這個函數可以保證交易價格在一定程度上與預期的價格相符，從而減少了由於價格波動而引起的滑點。
```
```
function swapExactTokensForTokens(
    uint amountIn,
    uint amountOutMin,
    address[] calldata path,
    address to,
    uint deadline
) external returns (uint[] memory amounts);
```

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

```
初始流動性鑄造時會扣除最低流動性。這種設計背後的理念是為了防止初始流動性提供者將過少的流動性添加到交易對中，從而影響AMM池的效能和效率。這種設計可以提高AMM池的效率和穩定性，並確保用戶在提供初始流動性時獲得公平的報酬。
```

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?
```
在UniswapV2Pair合約的mint函數中，用於計算新的流動性份額的公式是根據現有的流動性份額、新添加的代幣數量和UniswapV2的核心公式來計算的。這個核心公式通常被稱為“x * y = k”，其中x和y分別代表兩種代幣的數量，k是一個常數。通過使用特定的公式計算新的流動性份額，可以保持流動性提供者之間的公平競爭，同時防止任何一方通過大量添加或移除流動性來操縱市場價格。
```
## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

```
sandwich attack是一種在加密貨幣交易中的詐騙手法，其中惡意參與者在知道交易即將發生時，迅速進行兩筆相對的交易，使其在一筆交易之前和之後都進行操作。這樣的攻擊可以對交易方造成損失，因為交易價格可能因為這兩筆交易的操作而被操縱，導致交易方支付高於市場價格的價格進行交易。
```