document.addEventListener('DOMContentLoaded', () => {
    const addItem = document.getElementById('add_item');

    addItem.addEventListener('click', () => {
      const newLi = document.createElement('li');
      newLi.textContent = 'Item';

      const myList = document.querySelector('ul.my_list');

      myList.appendChild(newLi);
    });
  });
