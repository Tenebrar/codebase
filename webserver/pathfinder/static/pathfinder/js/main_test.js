class SubscriptedElement extends HTMLElement {
  constructor() {
    super();

    this.style_content();

    this.setAttribute('class', 'subscripted-wrapper');

    this.style_subscript();

    this.set_required_styling();
  }

  style_content() {
    /**
     * Move the content down into a div and move style and class to it (also add 'subscripted' class).
     * This is done to make sure style and class set to our custom element only affects the content and not the
     * subscript.
     */
    const new_content_element = document.createElement('div');

    new_content_element.innerHTML = this.innerHTML;
    this.innerHTML = null;

    new_content_element.setAttribute('style', this.getAttribute('style'));
    this.setAttribute('style', null);

    new_content_element.setAttribute('class', [this.getAttribute('class'), 'subscripted'].join(' '));
    this.removeAttribute('class');

    this.appendChild(new_content_element);
  }

  style_subscript() {
    /**
     * Add the required elements for creating the subscript. (Multiple elements were needed to get the centering and
     * resizing properties we wanted)
     */
    const subscript_wrapper = document.createElement('div');
    subscript_wrapper.setAttribute('class', 'subscript-wrapper');

    const subscript = document.createElement('div');
    subscript.setAttribute('class', [this.getAttribute('subscript-class'), 'subscript'].join(' '));

    subscript.setAttribute('style', this.getAttribute('subscript-style'));

    subscript.textContent = this.getAttribute('name');

    subscript_wrapper.appendChild(subscript);
    this.appendChild(subscript_wrapper);
  }

  set_required_styling() {
    /**
     * Add the styling required for our desired behaviour:
     * - A piece of content with a line of text below it (the subscript).
     * - Text should flow aligned with the content, but new lines should of course not overlap with the subscript.
     * - It must be possible to center the subscript.
     */
    const style = document.createElement('style');

    // subscripted has no required styling
    style.textContent = `
      .subscripted-wrapper {
        display: inline-flex;
        flex-direction: column;
      }

      .subscript-wrapper {
        display: flex;
      }
      
      .subscript {
        flex-grow: 1;
        width: 0;
      }
    `;
    this.appendChild(style);
  }
}

customElements.define('subscripted-element', SubscriptedElement);
