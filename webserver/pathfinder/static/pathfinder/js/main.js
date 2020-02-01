class SubscriptedElement extends HTMLElement {
  constructor() {
    super();

    this.style_content();

    this.setAttribute('class', [this.getAttribute('class'), 'subscripted-wrapper'].join(' '));

    this.style_subscript();

    this.set_required_styling();
  }

  style_content() {
    /**
     * Move the content down into a div and move style and class to it (also add 'subscripted' class).
     * This is done to make sure style and class set to our custom element only affects the content and not the
     * subscript.
     */
    const subscripted = document.createElement('div');

    subscripted.innerHTML = this.innerHTML;
    this.innerHTML = null;

    subscripted.setAttribute('style', this.getAttribute('subscripted-style'));
    this.removeAttribute('subscripted-style');
    subscripted.setAttribute('class', [this.getAttribute('subscripted-class'), 'subscripted'].join(' '));
    this.removeAttribute('subscripted-class');

    this.appendChild(subscripted);
  }

  style_subscript() {
    /**
     * Add the required elements for creating the subscript. (Multiple elements were needed to get the centering and
     * resizing properties we wanted)
     */
    const subscript_wrapper = document.createElement('div');
    subscript_wrapper.setAttribute('class', 'subscript-wrapper');

    const subscript = document.createElement('div');

    subscript.setAttribute('style', this.getAttribute('subscript-style'));
    this.removeAttribute('subscript-style');
    subscript.setAttribute('class', [this.getAttribute('subscript-class'), 'subscript'].join(' '));
    this.removeAttribute('subscript-class');

    subscript.textContent = this.getAttribute('subscript');

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
