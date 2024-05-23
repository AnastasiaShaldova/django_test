<template>
  <div>
    <h1>Список картинок</h1>
    <div class="upload-section">
      <input type="file" ref="fileInput" @change="handleFileInputChange">
      <input type="text" v-model="newImageData.description" placeholder="Введите описание">
      <button @click="addImage">Добавить изображение</button>
    </div>
    
    <div class="images-container">
      <div class="images-row" v-for="(chunk, index) in imagesChunked" :key="index">
        <div class="image-container" v-for="image in chunk" :key="image.id">
          <div class="image-wrapper">
            <img :src="`data:image/png;base64,${image.image}`" alt="Изображение" class="image">
          </div>
          <div class="description">{{ image.description }}</div>
          <button class="delete-button" @click="deleteImage(image.id)">Удалить</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
  .upload-section {
    margin-bottom: 20px;
  }

  .images-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 20px;
  }

  .images-row {
    width: 100%;
    display: flex;
    justify-content: space-between;
  }

  .image-container {
    flex: 0 0 calc(33.33% - 20px);
    margin-bottom: 20px;
    text-align: center;
  }

  .image-wrapper {
    width: 100%;
    height: 500px;
    overflow: hidden;
  }

  .image {
    width: 100%;
    height: auto;
  }

  .description {
    margin-top: 10px;
  }

  .delete-button {
    margin-top: 10px;
    background-color: red;
    color: white;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
  }
</style>

<script>
export default {
  data() {
    return {
      images: [],
      newImageData: {
        image: null,
        description: ''
      }
    };
  },
  computed: {
    imagesChunked() {
      const chunkSize = 3;
      const tempArray = [];

      for (let i = 0; i < this.images.length; i += chunkSize) {
        tempArray.push(this.images.slice(i, i + chunkSize));
      }

      return tempArray;
    }
  },
  created() {
    this.fetchImages();
  },
  methods: {
    fetchImages() {
      fetch('http://127.0.0.1:8000/api/image')
        .then(response => response.json())
        .then(data => {
          this.images = data;
        })
        .catch(error => {
          console.error('Ошибка при получении списка изображений:', error);
        });
    },
    deleteImage(id) {
      fetch(`http://127.0.0.1:8000/api/image/delete/${id}`, {
        method: 'DELETE'
      })
      .then(response => {
        if (response.ok) {
          this.fetchImages();
        } else {
          console.error('Ошибка при удалении изображения:', response.status);
        }
      })
      .catch(error => {
        console.error('Ошибка при удалении изображения:', error);
      });
    },
    handleFileInputChange(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = () => {
          this.newImageData.image = reader.result;
        };
        reader.readAsDataURL(file);
      }
    },
    addImage() {
      const formData = new FormData();
      formData.append('image', this.$refs.fileInput.files[0]);
      formData.append('description', this.newImageData.description);

      fetch('http://127.0.0.1:8000/api/image/create/', {
        method: 'POST',
        body: formData
      })
      .then(response => {
        if (response.ok) {
          this.fetchImages();
        } else {
          console.error('Ошибка при добавлении изображения:', response.status);
        }
      })
      .catch(error => {
        console.error('Ошибка при добавлении изображения:', error);
      });
    }
  }
};
</script>