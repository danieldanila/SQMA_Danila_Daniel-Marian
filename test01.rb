require 'rubygems'
require 'selenium-webdriver'

driver = Selenium::WebDriver.for :chrome
driver.get "https://collaborative.ase.ro/Pasul1.0.aspx"

sleep 2

element = driver.find_element :id => "RadioButton2"
element.click

sleep 2

element = driver.find_element :name => "Button1"
element.click

sleep 2

element = driver.find_element :id => "CheckBoxList1_0"
element.click

element = driver.find_element :id => "CheckBoxList1_4"
element.click

element = driver.find_element :id => "CheckBoxList1_9"
element.click

sleep 2

select_element = driver.find_element(name: 'ListBox1')
select = Selenium::WebDriver::Support::Select.new(select_element)
select.select_by(:text, '1.1. Aparate frigorifice de mari dimensiuni')
select.select_by(:text, '1.3. Aparate frigorifice / Congelatoare')
select.select_by(:text, '1.10. Plite electrice')

sleep 2

element = driver.find_element :name => "Button1"
element.click

sleep 2

element = driver.find_element :id => "CheckBoxList1_1"
element.click

sleep 2

select_element = driver.find_element(name: 'ListBox1')
select = Selenium::WebDriver::Support::Select.new(select_element)
select.select_by(:text, '2.2. Volumul (cantitatea) de DEEE tratate')
select.select_by(:text, '2.7. Consumul de energie pe unitatea de DEEE reciclat')

sleep 2

element = driver.find_element :name => "Button1"
element.click

sleep 2

element = driver.find_element :id => "TextBox00"
element.send_keys "1"

element = driver.find_element :id => "TextBox01"
element.send_keys "2"

element = driver.find_element :id => "TextBox10"
element.send_keys "3"

element = driver.find_element :id => "TextBox11"
element.send_keys "4"

element = driver.find_element :id => "TextBox20"
element.send_keys "5"

element = driver.find_element :id => "TextBox21"
element.send_keys "6"

sleep 2

element = driver.find_element :name => "Button1"
element.click

sleep 2

element = driver.find_element :name => "Button1"
element.click

sleep 2

element = driver.find_element :name => "ctl21"
element.send_keys "9"

sleep 2

element = driver.find_element :name => "ctl25"
element.click

sleep 2

element = driver.find_element :name => "Button1"
element.click

sleep 2

element = driver.find_element :name => "Button1"
element.click

sleep 2

driver.quit