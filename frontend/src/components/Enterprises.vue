<template>
    <div>
        <form @submit.prevent="submitForm">
          <div class="text-align-center">
            <h4>Cadastro de Empresas</h4>
          </div>
          <div class="form-group row">
            <input type="text" class="form-control col-3 mx-2" placeholder="Nome" v-model="enterprise.name">
            <input type="text" class="form-control col-3 mx-2" placeholder="Sobre" v-model="enterprise.about">
            <input type="text" class="form-control col-3 mx-2" placeholder="Documento" v-model="enterprise.doc">
            <input type="text" class="form-control col-3 mx-2" placeholder="Site" v-model="enterprise.site">
            <input type="checkbox" class="form-control col-3 mx-2" v-model="enterprise.active" checked="true" hidden="true">
            <button class="btn btn-success">Enviar</button>
          </div>
        </form>

        <hr>
        <Pagination :source="data" @navigate="navigate"/>
        <div class="table-responsive">
          <table class="table table-hover">
            <thead>
              <th>Nome</th>
              <th>Sobre</th>
              <th>Documento</th>
              <th>Site</th>
            </thead>
            <tbody>
              <tr v-for="enterprise in enterprises" :key="enterprise.id" @click="$data.enterprise = enterprise">
                <td>{{  enterprise.name }}</td>
                <td>{{  enterprise.about  }}</td>
                <td>{{  enterprise.doc  }}</td>
                <td>{{  enterprise.site }}</td>
                <td> 
                  <button class="btn btn-danger btn-sm mx-1" @click="showModal">x</button> 
                </td>              
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
            <button class="btn btn-danger btn-sm mx-1" @click="deleteEnterprise(enterprise)">Sim</button>
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

  name: 'Enterprises',

  data () {
    return {
      enterprise: {
        'name': '',
        'about': '',
        'site': '',
        'doc': '',
        'active': true
      },
      enterprises: [],
      data: [],
      isModalVisible: false,
    }
  },

  async created () {
    await this.getEnterprises()
  },

  methods: {
    handleErrors (response) {
      if (!response.ok) throw new Error(response.status)
      return response
    },

    navigate (page) {
      this.getEnterprises(page)
    },

    errorMessage () {
      window.alert("Ocorreu um erro com sua solicitação.")
    },

    async getEnterprises (page = 1) {
      var response = await fetch('http://localhost:8000/api/v1/enterprises/?page='+page)
      this.data = await response.json()
      this.enterprises = this.data.results
    },

    async submitForm () {
      if (this.enterprise.id === undefined) {
        this.createEnterprise()
      } else {
        this.editEnterprise()
      }
    },

    async createEnterprise () {
      var response = await fetch('http://localhost:8000/api/v1/enterprises/', {
        method: 'post',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(this.enterprise)
      }).then(
        this.handleErrors
      ).then(
        response => {
          return response
        }
      ).catch(
        error => this.errorMessage()
      )

      this.enterprises.push(await response.json())
    },

    async editEnterprise () {
      await this.getEnterprises()
      await fetch(`http://localhost:8000/api/v1/enterprises/${this.enterprise.id}/`, {
        method: 'put',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(this.enterprise)
      }).then(
        this.handleErrors
      ).then(
        response => {
          return response
        }
      ).catch(
        error => this.errorMessage()
      )

      this.enterprises = {}
      await this.getEnterprises()
    },

    async deleteEnterprise (enterprise) {
      await this.getEnterprises()
      await fetch(`http://localhost:8000/api/v1/enterprises/${enterprise.id}/`, {
        method: 'delete',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(this.enterprise)
      }).then(
        this.handleErrors
      ).then(
        response => {
          return response
        }
      ).catch(
        error => this.errorMessage()
      )

      this.enterprises = {}
      await this.getEnterprises()
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
