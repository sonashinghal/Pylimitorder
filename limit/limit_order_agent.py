import sys
import os
from typing import Protocol

current_dir = os.getcwd() # to resolve path issues

sys.path.append(current_dir)
from PyLimitOrders.trading_framework.execution_client import ExecutionClient
from PyLimitOrders.trading_framework.price_listener import PriceListener


class LimitOrderAgent(PriceListener):

    def _init_(self, execution_client: ExecutionClient, price_listener: PriceListener):
        # super()._init_()
        """
        :param execution_client: can be used to buy or sell - see ExecutionClient protocol definition
        # """
        self.execution_client = execution_client
        self.price_listener = price_listener
        # self.execution_client = execution_client
        # self.held_orders = []
    def add_order(self,bs_flag:str,product_id:int,amount:float,limit:int):
       
        if bs_flag == "b": #this is implementing buy
            self.on_price_tick(product_id, amount)  #on_price tick returns the control back to the calling program once the stock market price is target price
            self.execution_client.buy(product_id, limit)
           
        # assuming that price tick module will have a timeframe restriction so that it will wait  for the market price for the hit of markrt price
        elif(bs_flag == "s"): # this is implementing for sell
            self.on_price_tick(product_id, amount)
            self.execution_client.sell(product_id, limit)
        else:
            print("your Choice is wrong")  

if _name_ == "_main_":
    from PyLimitOrders.trading_framework.execution_client import ExecutionClient
    from PyLimitOrders.trading_framework.price_listener import PriceListener
    from typing import Protocol


    execution_client = ExecutionClient  # Assuming execution client is properly implemented
    price_listener = PriceListener
    agent = LimitOrderAgent(execution_client, price_listener)
    agent.add_order("s", 10, 10.00, 100)