<template>
    <div>
        <div id="citacao" v-for="usuario in usuarios" v-bind:key="usuario.id">
            <span> {{ usuario.author_quote }} </span><br>
            <span id=doautor>Id: <small id="autor"> {{ usuario.id }} </small></span><br>
            <span id=doautor>Autor: <small id="autor"> {{ usuario.author }} </small></span>
        </div>
    </div>
    
</template>

<style>
#citacao {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: left;
    background: #f6f897;
    color: black;
    max-width: 800px;
    min-width: 500px;
    min-height: 50px;
    padding: 10px;
    margin-bottom: 30px;
    border: 1px solid #333333;
    border-radius: 5px;
    box-shadow: 2px 2px 3px #333333;
}

#autor{
    color: #4582ec;
    font-weight: bold;
}

</style>

<script>
/*export default{
    name: 'Quote',
    props: {
        msg: String
    },
    data() {
        return{
            usuarios: [
                {id:1, nome: 'João'},
                {id:2, nome: 'Maria'},
                {id:3, nome: 'José'},
            ]
        }
    }

}*/

import axios from 'axios'

export default{
    data() {
        return{ 
            usuarios: [

            ]
        }
            
    },

    created() {
        axios.get("http://127.0.0.1:8000/quotes/")
            .then(response =>{
                this.usuarios = response.data;
            })
    }

}

/*import axios from 'axios'

export default {
   name: "author",
   citacao: "author_quote",
   data() {
     return {
       author: {},
       author_quote: {},
     };
   },
   created() {
     this.getUser();
   },
   methods: {
     getUser() {
       axios
         .get("http://127.0.0.1:8000/quotes/")
         .then((res) => {
           this.user = res.data;
         })
         .catch((error) => {
           console.log(error);
         });
     },
   },
  };*/

</script>