#function to calculate price after discunt

def apply_discount(price,discount):

   if not isinstance(price,(float,int)):
      return "The price should be a number"
   elif price<=0:
      return "The price should be greater than 0"

   if not isinstance(discount,(float,int)):
      return "The discount should be a number"
   elif discount<0 or discount>100:
      return "The discount should be between 0 and 100"

   return price-(price*discount/100)


       
    