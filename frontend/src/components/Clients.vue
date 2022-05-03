<template>
    <div>
        <form @submit.prevent="submitForm">
          <div class="text-align-center">
            <h4>Cadastro de Clientes</h4>
          </div>
          <div class="form-group row">
            <input type="text" class="form-control col-3 mx-2" placeholder="Nome" v-model="client.name">
            <input type="text" class="form-control col-3 mx-2" placeholder="Sobre" v-model="client.about">
            <input type="text" class="form-control col-3 mx-2" placeholder="Documento" v-model="client.doc">
            <input type="text" class="form-control col-3 mx-2" placeholder="Site" v-model="client.site">
            <input type="checkbox" class="form-control col-3 mx-2" v-model="client.active" checked="true" hidden="true">
            <button class="btn btn-success">Enviar</button>
          </div>
        </form>

        <hr>
        <Pagination :source="data" @navigate="navigate"/>
        <div class="table-responsive">
          <table class="table table-hover">
            <thead>
              <th scope="col">Nome</th>
              <th scope="col">Sobre</th>
              <th scope="col">Documento</th>
              <th scope="col">Site</th>
            </thead>
            <tbody>
              <tr scope="row" v-for="client in clients" :key="client.id" @click="$data.client = client">
                <td>{{  client.name }}</td>
                <td>{{  client.about  }}</td>
                <td>{{  client.doc  }}</td>
                <td>{{  client.site }}</td>
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
            Deseja realmente excluir este lance ? 
          </template>

          <template v-slot:footer>
            <button class="btn btn-danger btn-sm mx-1" @click="deleteClient(client)">Sim</button>
          </template>
        </Modal>
    </div>
</template>

<script>
import Pagination from './Pagination.vue'
import Modal from './modals/Modal.vue';

export default {
  components: { 
    Pagination,
    Modal
    },

  name: 'Clients',

  data () {
    return {
      client: {
        'name': '',
        'about': '',
        'site': '',
        'doc': '',
        'active': true
      },
      clients: [],
      data: [],
      isModalVisible: false,

    }
  },

  async created () {
    await this.getClients()
  },

  methods: {
    handleErrors (response) {
      if (!response.ok) throw new Error(response.status)
      return response
    },

    navigate (page) {
      this.getClients(page)
    },

    async getClients (page = 1) {
      var response = await fetch('http://localhost:8000/api/v1/clients/?page='+page)
      this.data = await response.json()
      this.clients = this.data.results
    },

    async submitForm () {
      if (this.client.id === undefined) {
        this.createClient()
      } else {
        this.editClient()
      }
    },

    async createClient () {
      var response = await fetch('http://localhost:8000/api/v1/clients/', {
        method: 'post',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(this.client)
      }).then(
        this.handleErrors
      ).then(
        response => {
          return response
        }
      ).catch(
        error => console.log(error)
      )
      this.clients.push(await response.json())
    },

    async editClient () {
      await fetch(`http://localhost:8000/api/v1/clients/${this.client.id}/`, {
        method: 'put',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(this.client)
      }).then(
        this.handleErrors
      ).then(
        response => {
          return response
        }
      ).catch(
        error => console.log(error)
      )
      this.client = {}
      await this.getClients()
    },

    async deleteClient (client) {
      await fetch(`http://localhost:8000/api/v1/clients/${client.id}/`, {
        method: 'delete',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(this.client)
      }).then(
        this.handleErrors
      ).then(
        response => {
          return response
        }
      ).catch(
        error => console.log(error)
      )
      this.client = {}
      this.getClients()
      this.closeModal()

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
</style>
