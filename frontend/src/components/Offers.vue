<template>
    <div>
        <form @submit.prevent="submitForm">
          <div class="text-align-center">
            <h4>Cadastro de Ofertas de Frete</h4>
          </div>
          <div class="form-group row">
            <input type="text" class="form-control col-3 mx-2" placeholder="De" v-model="offer.from">
            <input type="text" class="form-control col-3 mx-2" placeholder="Para" v-model="offer.to">
            <input type="number" class="form-control col-3 mx-2" placeholder="Valor Inicial" v-model="offer.initial_value">
            <input type="number" class="form-control col-3 mx-2" placeholder="Quantidade" v-model="offer.amount">
            <InputAmountType :source="offer"/>
            <InputCustomer :source="offer"/>
            <input type="checkbox" class="form-control col-3 mx-2" v-model="offer.active" checked="true" hidden="true">
            <button class="btn btn-success">Enviar</button>
          </div>
        </form>
        <hr>
        <Pagination :source="data" @navigate="navigate"/>
        <div class="table-responsive">
          <table class="table table-hover">
            <thead>
              <th>Id</th>
              <th>Cliente</th>
              <th>De</th>
              <th>Para</th>
              <th>Valor inicial</th>
              <th>Quantidade</th>
              <th>Tipo</th>
            </thead>
            <tbody>
              <tr v-for="offer in offers" :key="offer.id" @click="$data.offer = offer">
                <td>{{  offer.id }}</td>
                <td>{{  offer.id_customer.name }} </td>
                <td>{{  offer.from  }}</td>
                <td>{{  offer.to  }}</td>
                <td>R$ {{  offer.initial_value }}</td>
                <td>{{  offer.amount }}</td>
                <td>{{ getAmountType(offer) }}</td>
                <td><button class="btn btn-outline-primary" @click="goToBids(offer)">Lances</button></td>
                <td> <button class="btn btn-danger btn-sm mx-1" @click="showModal">x</button> </td>
              </tr>
            </tbody>
        </table>
        </div>

        <Modal v-show="isModalVisible" @close="closeModal">

          <template v-slot:header>
            Importante !
          </template>

          <template v-slot:body>
            Deseja realmente excluir esta oferta? 
          </template>

          <template v-slot:footer>
            <button class="btn btn-danger btn-sm mx-1" @click="deleteOffer(offer)">Sim</button>
          </template>
        </Modal>
    </div>
</template>

<script>
import Pagination from './Pagination.vue'
import InputCustomer from './inputs/InputCustomer.vue'
import InputAmountType from './inputs/InputAmountType.vue'
import Modal from './modals/Modal.vue';

export default {
  components: { 
    Pagination,
    InputCustomer,
    InputAmountType,
    Modal
    },

  name: 'Offers',

  data () {
    return {
      offer: {
      },
      offers: [],
      data: [],
      isModalVisible: false,

    }
  },

  async created () {
    await this.getOffers()
  },

  methods: {
    goToBids (offer) {
      this.$router.push({ name: 'bids', params: { id: offer.id } })
    },
    handleErrors (response) {
      if (!response.ok) throw new Error(response.status)
      return response
    },

    navigate (page) {
      this.getOffers(page)
    },

    errorMessage (error) {
      window.alert("Ocorreu um erro com sua solicitação." + error)
    },

    async getOffers (page = 1) {
      var response = await fetch('http://localhost:8000/api/v1/offers/?page='+page)
      this.data = await response.json()
      this.offers = this.data.results 
    },

    async submitForm () {
      if (this.offer.id === undefined) {
        this.createOffer()
      } else {
        this.editOffer()
      }
    },

    async createOffer () {
      var response = await fetch('http://localhost:8000/api/v1/offers/', {
        method: 'post',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(this.offer)
      }).then(
        this.handleErrors
      ).then(
        response => {
          return response
        }
      ).catch(
        error => this.errorMessage(error)
      )
      this.offers.push(await response.json())
      this.getOffers()
    },

    async editOffer () {
      await this.getOffers()
      await fetch(`http://localhost:8000/api/v1/offers/${this.offer.id}/`, {
        method: 'put',
        headers: {
          'Content-type': 'application/json'
        },
        
        body: JSON.stringify(this.offer)
      }).then(
        this.handleErrors
      ).then(
        response => {
          return response
        }
      ).catch(
        error => this.errorMessage(error)
      )

      this.offers = {}
      await this.getOffers()
    },

    async deleteOffer (offer) {
      await this.getOffers()
      await fetch(`http://localhost:8000/api/v1/offers/${offer.id}/`, {
        method: 'delete',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(this.offer)
      }).then(
        this.handleErrors
      ).then(
        response => {
          return response
        }
      ).catch(
        error => this.errorMessage(error)
      )

      this.offers = {}
      await this.getOffers()
      this.closeModal()

    },

    getAmountType (offer) {
      let type = '';
      if (offer.amount_type === "TON") {
        type = 'Toneladas'
      } else if (offer.amount_type === "KG") {
        type = 'Quilos'
      } 
      return type;
    },

    showModal() {
        this.isModalVisible = true;
      },

    closeModal() {
      this.isModalVisible = false;
    }
  }
}
</script>

<style scoped>
.bids {
  padding: 5px 0;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
</style>
