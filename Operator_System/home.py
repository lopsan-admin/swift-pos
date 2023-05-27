import kivy
import re

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label

class HomeWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.cart = []
        self.qty = []
        self.total = 0.00

    def update_purchases(self):
        prod_code = self.ids.product_code_input.text
        product_container = self.ids.products
        if prod_code == '1234' or prod_code == '2345':
            details = BoxLayout(size_hint_y = None, height = 30, pos_hint={'top': 1})
            product_container.add_widget(details)
            
            code = Label(text=prod_code, size_hint_x=.2, color=(19/255.0, 45/255.0, 70/255.0, 1))
            name = Label(text='Product One', size_hint_x=.3, color=(19/255.0, 45/255.0, 70/255.0, 1))
            qty = Label(text='1', size_hint_x=.1, color=(19/255.0, 45/255.0, 70/255.0, 1))
            discount = Label(text='0.00', size_hint_x=.1, color=(19/255.0, 45/255.0, 70/255.0, 1))
            price = Label(text='0.00', size_hint_x=.1, color=(19/255.0, 45/255.0, 70/255.0, 1))
            total = Label(text='0.00', size_hint_x=.1, color=(19/255.0, 45/255.0, 70/255.0, 1))
            details.add_widget(code)
            details.add_widget(name)
            details.add_widget(qty)
            details.add_widget(discount)
            details.add_widget(price)
            details.add_widget(total)

            #Update Preview
            prod_name = "Product One"
            if prod_code == '2345':
                prod_name = "Product Two"
            prod_price = 1.00
            prod_qty = str(1)
            self.total += prod_price
            purchase_total = "`\n\nTotal\t\t\t\t\t\t\t\t"+str(self.total)
            
            self.ids.cur_product.text = prod_name
            self.ids.cur_price.text = str(prod_price)
            
            preview = self.ids.receipt_preview
            prev_text = preview.text
            _prev = prev_text.find("`")
            if _prev > 0:
                prev_text =prev_text[:_prev]

            prod_target = -1
            for i, c in enumerate(self.cart):
                if c == prod_code:
                    prod_target = i

            if prod_target >= 0:
                prod_qty = self.qty[prod_target]+1
                self.qty[prod_target] = prod_qty
                expr = "%s\t\tx\d\t"%(prod_name)
                rexpr = prod_name+"\t\tx"+str(prod_qty)+"\t"
                nu_text = re.sub(expr, rexpr, prev_text)
                preview.text = nu_text + purchase_total
            else: 
                self.cart.append(prod_code)
                self.qty.append(1)
                new_preview = "\n".join([prev_text, prod_name+"\t\tx"+prod_qty+"\t\t"+str(prod_price),purchase_total])
                preview.text = new_preview

class HomeApp(App):
    def build(self):
        return HomeWindow()

if __name__=="__main__":
    ha = HomeApp()
    ha.run()