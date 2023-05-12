import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label

class HomeWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update_purchases(self):
        code = self.ids.product_code_input.text
        product_container = self.ids.products
        if code == '1234':
            details = BoxLayout(size_hint_y = None, height = 30, pos_hint={'top': 1})
            product_container.add_widget(details)
            
            code = Label(text=code, size_hint_x=.2, color=(19/255.0, 45/255.0, 70/255.0, 1))
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
            prod_price = 1.00
            preview = self.ids.receipt_preview
            prev_text = preview.text
            _prev = prev_text.find("`")
            if _prev > 0:
                prev_text =prev_text[:_prev]
            purchase_total = "`\n\nTotal\t\t\t\t\t\t\t\t0.00"
            new_preview = "\n".join([prev_text, prod_name+"\t\t\t\t"+str(prod_price),purchase_total])
            preview.text = new_preview

class HomeApp(App):
    def build(self):
        return HomeWindow()

if __name__=="__main__":
    ha = HomeApp()
    ha.run()