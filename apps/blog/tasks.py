"""
Tareas asincrónicas para el módulo de blog.
"""
from celery import shared_task


@shared_task
def suma_con_retardo(n1: int, n2: int) -> int:
    """
    Suma dos números con un retardo de 5 segundos
    :param n1: int
    :param n2: int
    :return: Suma de los dos números
    """
    from time import sleep
    print('Esperando 5 segundos')
    sleep(5)
    print('Listo!')
    return n1 + n2


@shared_task
def upload_cover_image(image_file: bytes, post_id: int) -> None:
    """
    Sube la imagen de portada de un post a Cloudinary
    :param image_file: Imagen en formato de bytes
    :param post_id: ID del posts al que pertenece la imagen
    """
    if image_file:
        from cloudinary.uploader import upload
        from apps.blog.models.post_model import Post

        try:
            # Subir la imagen a Cloudinary
            result = upload(image_file, folder='blog/')
            image_url = result.get('secure_url')

            # Obtener el objeto Post y actualizar la URL de la imagen de portada
            post = Post.objects.get(id=post_id)
            post.cover_image = image_url
            post.save()
        except Exception as e:
            print('Error:', e)

        # print('\n\n\n', result.get('secure_url'), '\n\n\n')
