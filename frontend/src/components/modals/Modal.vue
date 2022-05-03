<script>
  export default {
    name: 'Modal',
    methods: {
      close() {
        this.$emit('close');
      },
    },
  };
</script>

<template>
  <transition name="modal-fade ">
    <div class="modal-backdrop" >
      <div class="modal"  role="dialog">

        <header class="modal-header" id="modalTitle">
          <slot name="header">

          </slot>
          <button  type="button" class="btn-close" data-dismiss="modal" @click="close" aria-label="Close modal"> x </button>
        </header>

        <section class="modal-body" id="modalDescription" >
          <slot name="body">
          
          </slot>
        </section>

        <footer class="modal-footer">
          <div>
            <slot name="footer">
              
            </slot>
            <button type="button" class="btn btn-success btn-sm mx-1" @click="close" aria-label="Close modal"> Fechar </button>
          </div>
        </footer>
      </div>
    </div>
  </transition>
</template>

<style>
  .modal-backdrop {
    background-color: rgba(0, 0, 0, 0.3);
    display: block;
    justify-content: center;
    align-items: center;
    text-align: left;
    margin-left: auto;
    margin-right: auto;
  }

  .modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
    text-align: center;
    max-width: 500px;
    max-height: 210px;
    overflow: hidden;
    margin: 200px 0px 0 400px;
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    position: relative;
    border-bottom: 1px solid #eeeeee;
    color: #4AAE9B;
    justify-content: space-between;
  }

  .modal-footer {
    border-top: 1px solid #eeeeee;
    flex-direction: column;
  }

  .modal-body {
    position: relative;
    padding: 20px 10px;
  }

  .btn-close {
    position: absolute;
    top: 0;
    right: 0;
    border: none;
    font-size: 20px;
    padding: 10px;
    cursor: pointer;
    font-weight: bold;
    color: #4AAE9B;
    background: transparent;
  }

  .modal-fade-enter,
  .modal-fade-leave-to {
    opacity: 0;
  }

  .modal-fade-enter-active,
  .modal-fade-leave-active {
    transition: opacity .5s ease;
  }
</style>