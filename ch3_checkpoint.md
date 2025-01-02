{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/C109118214/AiAnalysic/blob/main/ch3_checkpoint.md\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6qx_kpjl-Vrm"
      },
      "source": [
        "# 範例 3-1"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "3ECy5V2J-Vro",
        "outputId": "57b8e4c3-33a7-4cc2-b901-03a088f1679b"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "10300.0"
            ]
          },
          "execution_count": 1,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "10000 * (1 + 0.03)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "IoDJQ9gC-Vrq",
        "outputId": "8569afde-acee-423d-bbfe-97b54e1a2ce6"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "10000.0\n"
          ]
        }
      ],
      "source": [
        "pv = 10000 * (1 + 0.03)\n",
        "print(pv / (1 + 0.03))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QZ29ESA9-Vrq"
      },
      "source": [
        "# 範例 3-2"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "knyeeAay-Vrr",
        "outputId": "b6e1ee79-3a59-4d29-a9ff-239072942fc6"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "1267650600228229401496703205376"
            ]
          },
          "execution_count": 1,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "2 ** 100"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "taFpnS1k-Vrr"
      },
      "source": [
        "# 範例 3-3"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "scrolled": true,
        "id": "fo8elHJ8-Vrr",
        "outputId": "973f48d7-8189-4559-c382-ae52cc2e23f5"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "5\n"
          ]
        }
      ],
      "source": [
        "data = 5\n",
        "print(data)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "to-EDP6b-Vrr"
      },
      "source": [
        "# 範例 3-4"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "l4cPrgcT-Vrr"
      },
      "outputs": [],
      "source": [
        "data = 50.5\n",
        "print(data)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FJimf9SD-Vrs"
      },
      "source": [
        "# 範例 3-5"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "DAviWHYD-Vrs",
        "outputId": "380298a8-ae85-471f-de1f-11ff65c50476"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Python is free\n"
          ]
        }
      ],
      "source": [
        "Str_X = \"Python \"\n",
        "Str_Y = \"is free\"\n",
        "print(Str_X + Str_Y)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "i7o2yBCZ-Vrs",
        "outputId": "d36df262-a831-40ae-e2b3-5b5ad9bf7116"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Python is freePython is freePython is free\n"
          ]
        }
      ],
      "source": [
        "print((Str_X + Str_Y) * 3)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "0WXz8BYQ-Vrs",
        "outputId": "542fb60d-17a9-4b83-ead2-d3c859f7d773"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "7\n"
          ]
        }
      ],
      "source": [
        "print(len(Str_X))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "g6HAV6H--Vrs"
      },
      "source": [
        "# 範例 3-6 ( 承接範例 3-5 )"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "CtcDmDbw-Vrs",
        "outputId": "4c37df2f-f69b-4179-b5cb-136c95aa2a29"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Python \n"
          ]
        }
      ],
      "source": [
        "print(Str_X[:])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "de2E43c5-Vrt",
        "outputId": "80fa070a-584d-4014-e2f5-4bc0ef44094f"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "t\n"
          ]
        }
      ],
      "source": [
        "print(Str_X[2])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "7VyW_9_B-Vrt",
        "outputId": "0cc0bcf1-217a-4381-b974-78211b5cdd96"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "n\n"
          ]
        }
      ],
      "source": [
        "print(Str_X[-2])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "KWY29EsQ-Vrt",
        "outputId": "a610197d-fff7-43c1-d121-7a1e24fa70f2"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            " \n"
          ]
        }
      ],
      "source": [
        "print(Str_X[-1])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sB43wUm2-Vrt"
      },
      "source": [
        "### 輸出一個空格"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "I9iWaxDh-Vrt",
        "outputId": "825e0619-54c3-47cf-ee8e-c6c441bebf0e"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "thon \n"
          ]
        }
      ],
      "source": [
        "print(Str_X[2 :])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "w8TIDa7j-Vrt",
        "outputId": "213c9beb-e8cc-4288-f965-dc3c3bb939c9"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            " nohtyP\n"
          ]
        }
      ],
      "source": [
        "print(Str_X[: : -1])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "brO27GZr-Vrt",
        "outputId": "2134be31-fc69-4a8f-e576-0fbe6d374a0c"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Pto \n"
          ]
        }
      ],
      "source": [
        "print(Str_X[0 : : 2])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gR6Pi-_M-Vru"
      },
      "source": [
        "# 範例 3-7"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "r9g7_vct-Vru",
        "outputId": "e53748dc-aa52-478d-b5bb-085616400cac"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Python is easy to learn\n"
          ]
        }
      ],
      "source": [
        "Str_Pyadv = \"python is Easy to Learn\"\n",
        "print(Str_Pyadv.capitalize( ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "wO7wrgsv-Vru",
        "outputId": "fe84496e-a4ce-4dc8-8eb8-97fdb243fafc"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "PYTHON IS EASY TO LEARN\n"
          ]
        }
      ],
      "source": [
        "print(Str_Pyadv.upper( ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "8CIk6YXG-Vru",
        "outputId": "da657916-bc8f-4f51-ad35-d17018b75962"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "python is easy to learn\n"
          ]
        }
      ],
      "source": [
        "print(Str_Pyadv.lower( ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "_x07cbmV-Vru",
        "outputId": "c838ba51-8a80-4459-af69-59aa19f605a2"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Python Is Easy To Learn\n"
          ]
        }
      ],
      "source": [
        "print(Str_Pyadv.title( ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "l-vZEme--Vru",
        "outputId": "bcab5f81-a4c2-43fa-bb55-857be68d78b2"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "PYTHON IS eASY TO lEARN\n"
          ]
        }
      ],
      "source": [
        "print(Str_Pyadv.swapcase( ))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SqCwKJUj-Vru"
      },
      "source": [
        "# 範例 3-8"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "SxNHGt-1-Vru",
        "outputId": "23e79c58-0bf1-4ff2-b243-8d687be7e1fe"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Python is Best for Beginners\n"
          ]
        }
      ],
      "source": [
        "Str_Py= \"Python is Good for Beginners\"\n",
        "print(Str_Py.replace(\"Good\", \"Best\"))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "hlg7ieG7-Vru",
        "outputId": "74f4513a-2d4f-490c-a224-6671f00e2569"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "7\n"
          ]
        }
      ],
      "source": [
        "print(Str_Py.find(\"is\"))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "0zNb2Cfu-Vrv",
        "outputId": "b2636494-cf78-486a-8848-3efe7da2ba59"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "3\n"
          ]
        }
      ],
      "source": [
        "print(Str_Py.count(\"n\"))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "2aj4LX97-Vrv",
        "outputId": "140a91b2-5852-47fe-a19d-c83967dc225e"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "True\n"
          ]
        }
      ],
      "source": [
        "print(Str_Py.startswith(\"for\", 15, 18))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "imzRyPKU-Vrv",
        "outputId": "5ad46589-1147-4c8f-d5e6-28d62ef697ed"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "['Python', 'is', 'Good for Beginners']\n"
          ]
        }
      ],
      "source": [
        "print(Str_Py.split(\" \", 2))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "7ML1CaKN-Vrv",
        "outputId": "597848ca-7bb0-44cf-a146-9db29e957048"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "2019-11-08\n"
          ]
        }
      ],
      "source": [
        "str_1 = \"-\"\n",
        "str_2 = (\"2019\", \"11\", \"08\")\n",
        "print(str_1.join(str_2))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "gomrRAQk-Vrv",
        "outputId": "b12c2380-9b74-4283-8445-c1a087753101"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Python is Good for Beginners\n"
          ]
        }
      ],
      "source": [
        "print(Str_Py)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "e_AyLuuU-Vrv",
        "outputId": "bc90edf3-cab5-4326-c4cf-aacdb303e9a8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Python is Best for Beginners\n"
          ]
        }
      ],
      "source": [
        "Str_Py = Str_Py.replace(\"Good\", \"Best\")\n",
        "print(Str_Py)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_h78Ch9--Vrv"
      },
      "source": [
        "# 範例 3-9"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "lY-bqJKe-Vrv",
        "outputId": "fc58180a-7ef7-4d3f-cdbc-31f3646ad201"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "True\n"
          ]
        }
      ],
      "source": [
        "Customer_Id = \"T124563210\"\n",
        "print(Customer_Id.isidentifier( ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "NhUKJV_i-Vr0",
        "outputId": "7d00805f-6279-4272-fc8f-cf73ab08702e"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "True\n"
          ]
        }
      ],
      "source": [
        "print(Customer_Id.isalnum( ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Hkis7ebH-Vr0",
        "outputId": "c852c5af-4cf5-422d-e95f-1f65a4fc3f7c"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "False\n"
          ]
        }
      ],
      "source": [
        "print(Customer_Id.isalpha( ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "59e0oE0b-Vr0",
        "outputId": "8302d873-e2a0-4260-ea03-7c92df5f5de0"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "True\n"
          ]
        }
      ],
      "source": [
        "print(Customer_Id[0].isalpha( ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "nrOXXnsF-Vr0",
        "outputId": "f740883f-02f2-4ff0-f11c-e3d6e58cdff0"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "False\n"
          ]
        }
      ],
      "source": [
        "print(Customer_Id.isdigit( ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "UxMkE3u7-Vr0",
        "outputId": "b8a3afc1-8dd0-45f1-c4e3-e2e9b6e531f3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "True\n"
          ]
        }
      ],
      "source": [
        "print(Customer_Id[1:10].isdigit( ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "wy6uxJR4-Vr0",
        "outputId": "f2a7a757-c409-467e-c20b-ee97e8908246"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "True\n"
          ]
        }
      ],
      "source": [
        "print(Customer_Id.isupper( ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HOeZK0wY-Vr1",
        "outputId": "8414d386-1b87-46c9-bff2-cd4d3e9af40d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "False\n"
          ]
        }
      ],
      "source": [
        "print(Customer_Id.islower( ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "fjfMX4G_-Vr1",
        "outputId": "e4b3540c-e384-44cf-ccd3-4c35dfa271ee"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "False\n"
          ]
        }
      ],
      "source": [
        "print(Customer_Id.isspace( ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "TK7sV1Ss-Vr1",
        "outputId": "7f87bb73-7c50-4e64-82a8-2fea5ef2f0a8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "True\n"
          ]
        }
      ],
      "source": [
        "print(\" \".isspace( ))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QcLyeKla-Vr1"
      },
      "source": [
        "# 範例 3-10"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "k_UOLy6M-Vr1",
        "outputId": "8e3a3b86-0adb-4d52-96ce-f393469e591c"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "['swimming', 1.5, 'run', 10, 'bike', 40]\n"
          ]
        }
      ],
      "source": [
        "Ironman = [\"swimming\", 1.5, \"run\", 10, \"bike\", 40]\n",
        "print(Ironman)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "DIfDmOeF-Vr1",
        "outputId": "343e80aa-25db-48e8-f7ad-8764ba01d141"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "['swimming', 1.5]\n"
          ]
        }
      ],
      "source": [
        "print(Ironman[0 : 2])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "aDobndgw-Vr1",
        "outputId": "14ebe16d-e860-4d72-e86b-dcbc23448baf"
      },
      "outputs": [
        {
          "ename": "IndexError",
          "evalue": "list index out of range",
          "output_type": "error",
          "traceback": [
            "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[1;32m<ipython-input-3-98c07d2b3db4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mIronman\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m10\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[1;31mIndexError\u001b[0m: list index out of range"
          ]
        }
      ],
      "source": [
        "print(Ironman[10])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6LTeGJT0-Vr1"
      },
      "source": [
        "# 範例 3-11"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "viz4o92X-Vr2"
      },
      "outputs": [],
      "source": [
        "Ary_A = [ ]\n",
        "Ary_A.append([6, 3, 1])\n",
        "print(Ary_A)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "aIN1BQ-J-Vr2",
        "outputId": "fd7a3c92-eb90-4d95-fe4e-49cb187f7c5f"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[[6, 3, 1], [5, 4, 3]]\n"
          ]
        }
      ],
      "source": [
        "Ary_A.extend([[5, 4, 3]])\n",
        "print(Ary_A)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Ndc8sawG-Vr2",
        "outputId": "35c77792-05de-470b-c671-93b3daf488a3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[[6, 3, 1], [3, 2, 1], [5, 4, 3]]\n"
          ]
        }
      ],
      "source": [
        "Ary_A.insert(1, [3, 2, 1])\n",
        "print(Ary_A)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Y8pCXFox-Vr2",
        "outputId": "b791d7de-e455-4a0c-a12f-ee71bb44ea7f"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "3\n"
          ]
        }
      ],
      "source": [
        "print(Ary_A[1][0])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "iAEBWRw6-Vr2",
        "outputId": "fefafada-7000-446b-d1c3-35da2b490ff1"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[[3, 2, 1], [5, 4, 3], [6, 3, 1]]\n"
          ]
        }
      ],
      "source": [
        "Ary_A.sort( )\n",
        "print(Ary_A)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "M1w-Nc-m-Vr2",
        "outputId": "0c1f6d5b-5520-4b35-e60d-329af633a7e3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[[6, 3, 1], [5, 4, 3], [3, 2, 1]]\n"
          ]
        }
      ],
      "source": [
        "Ary_A.sort(reverse = True)\n",
        "print(Ary_A)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "4s-tD3N6-Vr2",
        "outputId": "45139b21-5e09-4d0e-a913-2bc72caca2cc"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "[[6, 3, 1], [5, 4, 3], [3, 2, 1]]\n"
          ]
        }
      ],
      "source": [
        "Ary_B = Ary_A.copy( )\n",
        "print(Ary_B)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "BF6f0-ZY-Vr3"
      },
      "outputs": [],
      "source": [
        "Ary_B.clear( )"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "c9dOd2lC-Vr3"
      },
      "source": [
        "# 範例 3-12"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ksTaiMxg-Vr3"
      },
      "outputs": [],
      "source": [
        "List_Str = [\"ASUS\", \"BenQ\", \"GIANT\", \"ACER\"]\n",
        "print(List_Str[1 : 3])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "1uDyxpF1-Vr3",
        "outputId": "bf56c0c3-8c25-4b2f-8e34-01fd92c11e84"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "['ASUS', 'BenQ', 'GIANT', 'ACER']\n"
          ]
        }
      ],
      "source": [
        "print(List_Str)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "mnq7LcCC-Vr3",
        "outputId": "38479a99-0f25-4723-ca1c-047f298d88bc"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "['ASUS', 'BenQ', 'GIANT']\n"
          ]
        }
      ],
      "source": [
        "List_Str.remove(\"ACER\")\n",
        "print(List_Str)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Fbk2K_pc-Vr3",
        "outputId": "8dfbddac-e251-40e3-a0d1-0057e9bcaa03"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "GIANT\n"
          ]
        }
      ],
      "source": [
        "pop_value = List_Str.pop( )\n",
        "print(pop_value)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "fXA2Gr1D-Vr3",
        "outputId": "e0eaf756-d378-453a-fa48-18143141ad31"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "['ASUS', 'BenQ']\n"
          ]
        }
      ],
      "source": [
        "print(List_Str)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "BAilNsVd-Vr4",
        "outputId": "2b60cbc8-8316-47fb-df4e-85503bbce0c4"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "ASUS\n"
          ]
        }
      ],
      "source": [
        "pop_value = List_Str.pop(0)\n",
        "print(pop_value)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "7L2qcAsa-Vr4",
        "outputId": "75d081da-0872-4320-ce45-85a625004c89"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "['BenQ']\n"
          ]
        }
      ],
      "source": [
        "print(List_Str)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qSJuPNrV-Vr4"
      },
      "source": [
        "# 範例 3-13"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "oh-l4iZL-Vr4",
        "outputId": "773e5e69-65f6-404f-9a5b-07da73e155e7"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "('H234543783', 90.21, 88)\n"
          ]
        }
      ],
      "source": [
        "Tup_GradeInfo= (\"H234543783\", 90.21, 88)\n",
        "print(Tup_GradeInfo)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "YB3mrYCO-Vr4",
        "outputId": "261e3f80-d6e1-4e6b-d3b4-9ef5668f6d55"
      },
      "outputs": [
        {
          "ename": "TypeError",
          "evalue": "'tuple' object does not support item assignment",
          "output_type": "error",
          "traceback": [
            "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[1;32m<ipython-input-2-19756004bf8b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mTup_GradeInfo\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m90\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[1;31mTypeError\u001b[0m: 'tuple' object does not support item assignment"
          ]
        }
      ],
      "source": [
        "Tup_GradeInfo[1] = 90"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9arfipcc-Vr4"
      },
      "source": [
        "# 範例 3-14"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "eWMHJzGp-Vr4",
        "outputId": "556e716c-5572-4398-95cd-35573990a299"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'C', 'A', 'B'}\n"
          ]
        }
      ],
      "source": [
        "Set_CreditClass = {\"A\", \"B\", \"C\", \"C\"}\n",
        "print(Set_CreditClass)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VrwwZfyT-Vr4"
      },
      "source": [
        "### set 沒有順序性，故此結果與書本不同"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "reGHtgY2-Vr5",
        "outputId": "4ad55404-ecd6-4a98-9fba-b78dddd78c59"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{226, 3.8, 42.2, 180, 'Super Ironman'}\n"
          ]
        }
      ],
      "source": [
        "Set_LegalDT = {\"Super Ironman\", 3.8, 180, 42.2, (226)}\n",
        "print(Set_LegalDT)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "5kDK8YOz-Vr5",
        "outputId": "47403f3b-407a-485e-eeb2-cb6a6b2852ef"
      },
      "outputs": [
        {
          "ename": "TypeError",
          "evalue": "unhashable type: 'set'",
          "output_type": "error",
          "traceback": [
            "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[1;32m<ipython-input-3-a2fa0d501990>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mSet_Set\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m6\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[1;31mTypeError\u001b[0m: unhashable type: 'set'"
          ]
        }
      ],
      "source": [
        "Set_Set = {{2, 5, 6}}"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "50S5J3VZ-Vr5",
        "outputId": "20fbd5eb-d84c-460a-ec1c-11e8cecf941c"
      },
      "outputs": [
        {
          "ename": "TypeError",
          "evalue": "unhashable type: 'list'",
          "output_type": "error",
          "traceback": [
            "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[1;32m<ipython-input-4-53e360093e86>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mSet_List\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m66\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m78\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m91\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[1;31mTypeError\u001b[0m: unhashable type: 'list'"
          ]
        }
      ],
      "source": [
        "Set_List = {[66, 78, 91]}"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "5WV9h5iN-Vr5",
        "outputId": "b9946be0-aa5a-4499-cad9-e45b8a95106e"
      },
      "outputs": [
        {
          "ename": "TypeError",
          "evalue": "unhashable type: 'dict'",
          "output_type": "error",
          "traceback": [
            "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[1;32m<ipython-input-5-f8c068bf2dd7>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mSet_Dict\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m{\u001b[0m\u001b[1;36m2330\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\" 台積電\"\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[1;31mTypeError\u001b[0m: unhashable type: 'dict'"
          ]
        }
      ],
      "source": [
        "Set_Dict = {{2330: \" 台積電\"}}"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bP4qovCg-Vr5"
      },
      "source": [
        "# 範例 3-15"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "GB3zTGXy-Vr5",
        "outputId": "d3527fd2-5117-4cb3-d0f0-b94ffd90a4a1"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'Red', 'Blue', 'Black', 'Green'}\n"
          ]
        }
      ],
      "source": [
        "Set_Color_A = { }\n",
        "Set_Color_A = {\"Red\", \"Green\", \"Blue\", \"Black\"}\n",
        "print(Set_Color_A)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "rmcC0shi-Vr5",
        "outputId": "931e0256-f10a-4b68-a6a5-4041c4028c96"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'Green', 'Blue', 'Red', 'Yellow', 'Black'}\n"
          ]
        }
      ],
      "source": [
        "Set_Color_A.add(\"Yellow\")\n",
        "print(Set_Color_A)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "wOlv2ECG-Vr5",
        "outputId": "3baa31ab-a0af-48f2-99bc-56a0c1c0c3a6"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'Green', 'Red', 'Yellow', 'Black'}\n"
          ]
        }
      ],
      "source": [
        "Set_Color_A.remove(\"Blue\")\n",
        "print(Set_Color_A)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "DqjBJq20-Vr6",
        "outputId": "81e06377-bde7-4250-e7d6-d6261982bcde"
      },
      "outputs": [
        {
          "ename": "KeyError",
          "evalue": "'Pink'",
          "output_type": "error",
          "traceback": [
            "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
            "\u001b[1;32m<ipython-input-4-50d40ece8aa1>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mSet_Color_A\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mremove\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Pink\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[1;31mKeyError\u001b[0m: 'Pink'"
          ]
        }
      ],
      "source": [
        "Set_Color_A.remove(\"Pink\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "A5qtKtfu-Vr6",
        "outputId": "ac0f2333-8fac-4341-bf70-9591ab287d15"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'Green', 'Red', 'Black'}\n"
          ]
        }
      ],
      "source": [
        "Set_Color_A.discard(\"Yellow\")\n",
        "print(Set_Color_A)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "lzzIObgQ-Vr6",
        "outputId": "875263f9-aa57-4c3a-9499-6144b36e447e"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'Green', 'Red', 'Black'}\n"
          ]
        }
      ],
      "source": [
        "Set_Color_A.discard(\"Pink\")\n",
        "print(Set_Color_A)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Pzm24_Ws-Vr6",
        "outputId": "a36085b4-be60-4161-95ac-a2832254d640"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Green\n"
          ]
        }
      ],
      "source": [
        "Pop_Value = Set_Color_A.pop( )\n",
        "print(Pop_Value)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "BuCvo_TG-Vr7"
      },
      "source": [
        "### set 沒有順序性，故此處結果與書本不同"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "4Wu_dPNx-Vr7",
        "outputId": "0e3eeff9-d9a2-44c4-aebb-b0bb2495f3d5"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "set()\n"
          ]
        }
      ],
      "source": [
        "Set_Color_A.clear( )\n",
        "print(Set_Color_A)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ieRmQchA-Vr7",
        "outputId": "7fbc3246-1bce-4a82-9541-404595c1f501"
      },
      "outputs": [
        {
          "ename": "KeyError",
          "evalue": "'pop from an empty set'",
          "output_type": "error",
          "traceback": [
            "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
            "\u001b[1;32m<ipython-input-9-105f609e1545>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mSet_Color_A\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpop\u001b[0m\u001b[1;33m(\u001b[0m \u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[1;31mKeyError\u001b[0m: 'pop from an empty set'"
          ]
        }
      ],
      "source": [
        "Set_Color_A.pop( )"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "F0TDu_JB-Vr7"
      },
      "source": [
        "# 範例 3-16"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "jpizUVuz-Vr7",
        "outputId": "fc85e62a-69d6-42c3-8005-e12848ee713b"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 1,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Set_One = {1, 2, 3, 4, 5}\n",
        "Set_Two = {3, 4, 5}\n",
        "Set_One.issuperset(Set_Two)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "hA7ZScHi-Vr7",
        "outputId": "ece9acbe-f595-4c43-f84b-958acb244740"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 2,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Set_Two.issubset(Set_One)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "jYlCdtD6-Vr7"
      },
      "outputs": [],
      "source": [
        "Set_Color_A = {\"Red\", \"Green\", \"Blue\", \"Black\", \"Yellow\"}\n",
        "Set_Color_B = {\"Grey\", \"Black\", \"White\", \"Yellow\"}"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Ybcf9kVc-Vr7",
        "outputId": "0a5b69e0-2481-458d-d4c0-0d9ae9112ad0"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "{'Black', 'Blue', 'Green', 'Grey', 'Red', 'White', 'Yellow'}"
            ]
          },
          "execution_count": 4,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Set_Color_A.union(Set_Color_B)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "RltozIPf-Vr8",
        "outputId": "135829bc-2acd-40d4-c196-e1d558d7fbaf"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "{'Black', 'Blue', 'Green', 'Grey', 'Red', 'White', 'Yellow'}"
            ]
          },
          "execution_count": 5,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Set_Color_A | Set_Color_B"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "fCKbCXBr-Vr8",
        "outputId": "1c953da5-2a98-40a6-83a0-066f4b5bffc7"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "{'Black', 'Yellow'}"
            ]
          },
          "execution_count": 6,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Set_Color_A.intersection(Set_Color_B)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "NB2hgFPz-Vr8",
        "outputId": "6a637165-8223-40be-e5b0-73b844455415"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "{'Black', 'Yellow'}"
            ]
          },
          "execution_count": 7,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Set_Color_A & Set_Color_B"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ez8pneWB-Vr8",
        "outputId": "8a38f39c-6622-4ee2-f451-23deabae429a"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "{'Blue', 'Green', 'Red'}"
            ]
          },
          "execution_count": 8,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Set_Color_A.difference(Set_Color_B)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "PsZqoTpW-Vr8",
        "outputId": "27b0e1b1-3a1c-4dbd-b0a8-fc4f49a5e21c"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "{'Blue', 'Green', 'Red'}"
            ]
          },
          "execution_count": 9,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Set_Color_A - Set_Color_B"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Ckb0qJhh-Vr8"
      },
      "source": [
        "# 範例 3-17"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "43YJXiiR-Vr8",
        "outputId": "03b112f1-7c1f-40b5-c4da-e504f80f9d07"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'Name': 'Steven', 'Age': 25, 'Investment': 1000.25}\n"
          ]
        }
      ],
      "source": [
        "Dict_C1 = {\"Name\": \"Steven\", \"Age\": 25, \"Investment\":1000.25}\n",
        "print(Dict_C1)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "LA1Jfs_Z-Vr9",
        "outputId": "bcdd10f7-689c-4299-a037-93dd96a2eb27"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'Name': 'Steven', 'Age': 25, 'Investment': 1000.25, 'Email': 'Steven@gmail.com'}\n"
          ]
        }
      ],
      "source": [
        "Dict_C1[ \"Email\" ] = \"Steven@gmail.com\"\n",
        "print(Dict_C1)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jrIc8J7y-Vr9"
      },
      "source": [
        "# 範例 3-18"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "_aOQtdXx-Vr9",
        "outputId": "e42af548-22f1-45b6-eeea-50c3b6277866"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Bob\n"
          ]
        }
      ],
      "source": [
        "Dict_C3 = {'Name': 'Bob', 'Age': 27, 'Investment': 2500.33}\n",
        "print(Dict_C3[\"Name\"])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "LaWH26ae-Vr9",
        "outputId": "c3e9b260-3e90-4c12-b0bc-15191abb8e53"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Bob\n"
          ]
        }
      ],
      "source": [
        "print(Dict_C3.get(\"Name\"))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "NkIAE8bP-Vr9",
        "outputId": "06239d6d-d7a4-4dff-cfd6-5a9ab95df4aa"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "None\n"
          ]
        }
      ],
      "source": [
        "print(Dict_C3.get(\"name\"))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ktIVBNuK-Vr9",
        "outputId": "96691cd5-c612-4f78-bc84-75c51341edd3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "dict_items([('Name', 'Bob'), ('Age', 27), ('Investment', 2500.33)])\n"
          ]
        }
      ],
      "source": [
        "print(Dict_C3.items( ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "BXHr0vQA-Vr9",
        "outputId": "848290d4-dabd-493b-defb-f5bc4a7902b0"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "dict_keys(['Name', 'Age', 'Investment'])\n"
          ]
        }
      ],
      "source": [
        "print(Dict_C3.keys( ))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "5xMoP93h-Vr-",
        "outputId": "7f60a309-6e0d-4d58-f5e9-3340614081aa"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "dict_values(['Bob', 27, 2500.33])\n"
          ]
        }
      ],
      "source": [
        "print(Dict_C3.values( ))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fJ-eBWxF-Vr-"
      },
      "source": [
        "# 範例 3-19"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "yliftaPC-Vr-",
        "outputId": "1e13b09d-a37f-485d-ab2c-e57744304807"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'Name': 'Jonathan', 'Age': 26, 'Investment': 1200.3}\n"
          ]
        }
      ],
      "source": [
        "Dict_C2 = {'Name': 'Jonathan', 'Age': 26, 'Investment': 1200.3}\n",
        "print(Dict_C2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cm3iizzk-Vr-",
        "outputId": "e2044a5e-0062-4925-f7e8-3f87ba58e925"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'Name': 'Jonathan', 'Age': 36, 'Investment': 1200.3}\n"
          ]
        }
      ],
      "source": [
        "Dict_C2.update({\"Age\": 36})\n",
        "print(Dict_C2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "J4kbDIwC-Vr-",
        "outputId": "3a5a4e1b-394f-42c5-89ed-3051b11dc88d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'Name': 'Jonathan', 'Age': 36, 'Investment': 1200.3, 'Sex': 1}\n"
          ]
        }
      ],
      "source": [
        "Dict_C2.update({\"Sex\" : 1})\n",
        "print(Dict_C2)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6k21XiWc-Vr-"
      },
      "source": [
        "# 範例 3-20 ( 接續範例 3-18 )"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "YFIVFN-U-Vr-",
        "outputId": "f2a111d4-7d8c-46e4-93d0-0404d929733a"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'Name': 'Bob', 'Age': 27, 'Investment': 2500.33}\n"
          ]
        }
      ],
      "source": [
        "Temp = Dict_C3.copy( )\n",
        "print(Temp)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "BKooLWjv-Vr-",
        "outputId": "adccaa19-4c19-4148-bb1f-452dbc1c3f87"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'Name': 'Bob', 'Age': 27}\n"
          ]
        }
      ],
      "source": [
        "del Temp[\"Investment\"]\n",
        "print(Temp)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "YfdOB8wN-Vr-",
        "outputId": "b65c71e6-ff77-4271-ebf8-b6e57c8d90d2"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "27\n"
          ]
        }
      ],
      "source": [
        "RetValue = Temp.pop(\"Age\")\n",
        "print(RetValue)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "EcoKFEOe-Vr_",
        "outputId": "afe3edd1-de23-4dd5-b814-337ed01cedf9"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'CusName': 'Bob'}\n"
          ]
        }
      ],
      "source": [
        "Temp[\"CusName\"] = Temp.pop(\"Name\")\n",
        "print(Temp)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "vPB0SbaV-Vr_",
        "outputId": "f0be3f4a-b345-43b7-9333-25aa7e72cabd"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{}\n"
          ]
        }
      ],
      "source": [
        "Temp.clear( )\n",
        "print(Temp)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3xvAZ98G-Vr_"
      },
      "source": [
        "# 範例 3-21"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ICqTda5V-Vr_",
        "outputId": "6e103c29-d9f3-415e-ff88-0021fe957c5b"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "12"
            ]
          },
          "execution_count": 1,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Num_A = 10\n",
        "Num_B = 2\n",
        "Num_A + Num_B"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "J24Sc-rG-Vr_",
        "outputId": "fa90951c-1b2b-4f98-9268-98a11ae5c588"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "8"
            ]
          },
          "execution_count": 2,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Num_A - Num_B"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "AEwfaBEq-Vr_",
        "outputId": "8bc13ddb-9a80-4798-d964-d0d10b101e20"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "20"
            ]
          },
          "execution_count": 3,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Num_A * Num_B"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "K1TbhWl--VsA",
        "outputId": "b31d62ac-8578-430d-b901-686ae8d7dc27"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "1.0"
            ]
          },
          "execution_count": 4,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Num_A / Num_A"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "XTQLCoTF-VsA",
        "outputId": "a17ce351-f5df-4637-dafa-d231dac68025"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "execution_count": 5,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Num_A // 4"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Sn5Wfws6-VsA",
        "outputId": "f2ac05a2-32b3-4fa6-c28d-cbb107ddc0e3"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "100"
            ]
          },
          "execution_count": 6,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Num_A ** Num_B"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "JRrnod-4-VsA",
        "outputId": "23cac03c-8ddc-48e9-ef5a-67ea475c955b"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "execution_count": 7,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Num_A % Num_B"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8zkdaidj-VsA"
      },
      "source": [
        "# 範例 3-22 ( 接續範例 3-21 )"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "n6VhrOEW-VsB",
        "outputId": "9cd4727a-81a6-4079-b5a8-6bb0e724a8b5"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 8,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Num_A > Num_B"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "oS04cuFr-VsB",
        "outputId": "026565ca-d931-4185-ca26-ccf4ef1fa96b"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "execution_count": 9,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Num_A <= Num_B"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "wKDddXiX-VsB",
        "outputId": "a5ef5e00-9c6c-484b-8fb8-a940c583c41b"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 10,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Num_A != Num_B"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "oOPSPzIr-VsB",
        "outputId": "22984f8d-0523-42dc-be56-827899433e5a"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "execution_count": 11,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Num_A == Num_B"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Q-b42_jd-VsB"
      },
      "source": [
        "# 範例 3-23 ( 接續範例 3-22 )"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "vwoN_grN-VsB",
        "outputId": "16d86434-e86e-4da1-f99b-7b20cf131bb4"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "True\n"
          ]
        }
      ],
      "source": [
        "Cond_A = Num_A != Num_B\n",
        "print(Cond_A)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "zZtn2f5N-VsB",
        "outputId": "738be3ff-95e1-40be-c529-85fc9d32c9d3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "False\n"
          ]
        }
      ],
      "source": [
        "Cond_B = Num_A == Num_B\n",
        "print(Cond_B)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "OJdk9jk8-VsB",
        "outputId": "dc27db96-0c05-4310-b201-ca2ed14a6728"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 14,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Cond_A or Cond_B"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "T6UJm9YB-VsB",
        "outputId": "b1659be2-ab48-4219-f207-aad627b3e546"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "execution_count": 15,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "Cond_A and Cond_B"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ocoN4Ctt-VsC",
        "outputId": "72601f34-d57b-453d-9f39-9fb362e03789"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "execution_count": 16,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "not Cond_A"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "u3wMV9xz-VsC",
        "outputId": "9f021d8d-cea2-469f-a286-c2dacd499bd9"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 17,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "not Cond_B"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fSZEqYwf-VsC"
      },
      "source": [
        "# 範例 3-24"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ICkTJ9jR-VsC",
        "outputId": "60488ee7-2e00-46dd-a468-99cceaa865ce"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'int'>\n"
          ]
        }
      ],
      "source": [
        "Num_X = 5\n",
        "print(type(Num_X))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "hPwy4JgX-VsC",
        "outputId": "770b78cc-41fa-41f0-8294-de8302b75994"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "execution_count": 2,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "callable(Num_X)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "5IDFP7Rh-VsC",
        "outputId": "507b5c6f-6e77-41b7-99f6-99f3a2ee9924"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 3,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "callable(int)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "8ljCn7Ta-VsC",
        "outputId": "5192d22b-950c-4c47-c580-8fda32747b8e"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "execution_count": 4,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "isinstance(Num_X, int)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "OJOjPPZ9-VsD",
        "outputId": "8182fba2-96d6-47c2-d675-2e5c290f305a"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "['__add__',\n",
              " '__class__',\n",
              " '__contains__',\n",
              " '__delattr__',\n",
              " '__dir__',\n",
              " '__doc__',\n",
              " '__eq__',\n",
              " '__format__',\n",
              " '__ge__',\n",
              " '__getattribute__',\n",
              " '__getitem__',\n",
              " '__getnewargs__',\n",
              " '__gt__',\n",
              " '__hash__',\n",
              " '__init__',\n",
              " '__init_subclass__',\n",
              " '__iter__',\n",
              " '__le__',\n",
              " '__len__',\n",
              " '__lt__',\n",
              " '__mod__',\n",
              " '__mul__',\n",
              " '__ne__',\n",
              " '__new__',\n",
              " '__reduce__',\n",
              " '__reduce_ex__',\n",
              " '__repr__',\n",
              " '__rmod__',\n",
              " '__rmul__',\n",
              " '__setattr__',\n",
              " '__sizeof__',\n",
              " '__str__',\n",
              " '__subclasshook__',\n",
              " 'capitalize',\n",
              " 'casefold',\n",
              " 'center',\n",
              " 'count',\n",
              " 'encode',\n",
              " 'endswith',\n",
              " 'expandtabs',\n",
              " 'find',\n",
              " 'format',\n",
              " 'format_map',\n",
              " 'index',\n",
              " 'isalnum',\n",
              " 'isalpha',\n",
              " 'isascii',\n",
              " 'isdecimal',\n",
              " 'isdigit',\n",
              " 'isidentifier',\n",
              " 'islower',\n",
              " 'isnumeric',\n",
              " 'isprintable',\n",
              " 'isspace',\n",
              " 'istitle',\n",
              " 'isupper',\n",
              " 'join',\n",
              " 'ljust',\n",
              " 'lower',\n",
              " 'lstrip',\n",
              " 'maketrans',\n",
              " 'partition',\n",
              " 'replace',\n",
              " 'rfind',\n",
              " 'rindex',\n",
              " 'rjust',\n",
              " 'rpartition',\n",
              " 'rsplit',\n",
              " 'rstrip',\n",
              " 'split',\n",
              " 'splitlines',\n",
              " 'startswith',\n",
              " 'strip',\n",
              " 'swapcase',\n",
              " 'title',\n",
              " 'translate',\n",
              " 'upper',\n",
              " 'zfill']"
            ]
          },
          "execution_count": 5,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "dir(str)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "y39FimD1-VsD",
        "outputId": "9d90511a-3863-4905-9c02-35b2b884961e"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Help on built-in function print in module builtins:\n",
            "\n",
            "print(...)\n",
            "    print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)\n",
            "    \n",
            "    Prints the values to a stream, or to sys.stdout by default.\n",
            "    Optional keyword arguments:\n",
            "    file:  a file-like object (stream); defaults to the current sys.stdout.\n",
            "    sep:   string inserted between values, default a space.\n",
            "    end:   string appended after the last value, default a newline.\n",
            "    flush: whether to forcibly flush the stream.\n",
            "\n"
          ]
        }
      ],
      "source": [
        "help(print)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pFw2y-N1-VsD"
      },
      "source": [
        "# 範例 3-25"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "OozXXU9M-VsD",
        "outputId": "1d65e516-5bc0-4d5c-8a46-355fee11bc19"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "0b1100100\n"
          ]
        }
      ],
      "source": [
        "Num_Y = 100\n",
        "print( bin( Num_Y ) )"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "N-zq4Ejv-VsD",
        "outputId": "3fffd272-2c6d-4451-c26e-da0a23649cfc"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "0o144\n"
          ]
        }
      ],
      "source": [
        "print(oct(Num_Y))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "s7Mw6j2_-VsD",
        "outputId": "247b9efc-8726-4a0d-f60d-8f4ef886b937"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "0x64\n"
          ]
        }
      ],
      "source": [
        "print(hex (Num_Y))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "deqf24LX-VsD",
        "outputId": "d7f99894-5f8b-4a2c-89a3-7172e67dc88d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "d\n"
          ]
        }
      ],
      "source": [
        "print(chr(Num_Y))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HIWAEsvU-VsD",
        "outputId": "39bef889-9e4a-4658-fb30-73741791f09d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "100\n"
          ]
        }
      ],
      "source": [
        "print(ord('d'))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "vZ1P8E2R-VsE",
        "outputId": "7c6f28ce-a949-4f80-df60-2e97d6e9d609"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'str'>\n"
          ]
        }
      ],
      "source": [
        "Str_Rate = \"0.0115\"\n",
        "print(type(Str_Rate))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "iI5en72B-VsE",
        "outputId": "2587e38d-0a20-440c-f9c9-f80b892326d3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "0.0115\n"
          ]
        }
      ],
      "source": [
        "Float_Rate = float(Str_Rate)\n",
        "print(Float_Rate)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "zJMWF8Jh-VsE",
        "outputId": "064daf66-3328-44f2-838e-0245a1360704"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'float'>\n"
          ]
        }
      ],
      "source": [
        "print(type(Float_Rate))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "DHPEZnI7-VsE",
        "outputId": "abdab6a9-a059-4bdb-c5d2-ce67b6795307"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "115.0\n"
          ]
        }
      ],
      "source": [
        "print(Float_Rate * 10000)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "R6eNfK0k-VsE",
        "outputId": "2af1ff4b-db74-4a40-ef83-85c13a39d7ec"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "115\n"
          ]
        }
      ],
      "source": [
        "print(int (Float_Rate * 10000))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "q01kydmp-VsE"
      },
      "source": [
        "# 範例 3-26"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "w9nm4EZp-VsE",
        "outputId": "b8abd689-e0d1-4dbb-968f-187e001a838e"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "3\n"
          ]
        }
      ],
      "source": [
        "print(abs(-3))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "xX0396Zp-VsE",
        "outputId": "587e120f-1e8d-4839-9301-adf51e680ec3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "8\n"
          ]
        }
      ],
      "source": [
        "print(pow(2 , 3))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "4XzbpC3P-VsF",
        "outputId": "006a328a-40ce-41c0-e19a-36688ec1d037"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "4.12\n"
          ]
        }
      ],
      "source": [
        "print(round(4.1204 , 2))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "odeqSMbk-VsF",
        "outputId": "43757b6e-a8eb-4193-c4ab-531702fc68a5"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "(3, 1)\n"
          ]
        }
      ],
      "source": [
        "print(divmod(10 , 3))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "VdP8hJcO-VsF",
        "outputId": "2c52e9b5-d9a2-43ad-9092-b500dd13cd89"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "9\n"
          ]
        }
      ],
      "source": [
        "Sample = [5, 8, 9, 6, 4, 1, 5, 3, 6, 2]\n",
        "print(max(Sample))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cI7asGxe-VsF",
        "outputId": "86a3796c-9099-454d-fe83-c90f07f13188"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "1\n"
          ]
        }
      ],
      "source": [
        "print(min(Sample))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "O5rIGioq-VsF",
        "outputId": "f442b010-3a70-453b-e6b7-6956b86ba930"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "49\n"
          ]
        }
      ],
      "source": [
        "print(sum(Sample))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "YzcYV1EO-VsF",
        "outputId": "e3382036-3224-4024-b6ef-6f29b2c95a88"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "10\n"
          ]
        }
      ],
      "source": [
        "print(len(Sample))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "81W5Ecfk-VsF"
      },
      "source": [
        "# 範例 3-27"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "N8Ua10z--VsF",
        "outputId": "703c00ea-67f5-4978-af9c-4431409026e1"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            " 請輸入年利率 = 0.0115\n",
            "0.0115\n"
          ]
        }
      ],
      "source": [
        "Interest = input(\" 請輸入年利率 = \")\n",
        "請輸入年利率 = 0.0115\n",
        "print(Interest)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "7NCR0XlK-VsG",
        "outputId": "b4b69634-8709-47b4-8c8a-c3ad13760e72"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "<class 'str'>\n"
          ]
        }
      ],
      "source": [
        "print(type(Interest))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9KUxG5Mg-VsG"
      },
      "source": [
        "# 範例 3-28"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "aGWkawYi-VsG",
        "outputId": "e2a64a90-cee3-411e-9c60-713019aceff6"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            " 請輸入年利率 = 0.0115\n"
          ]
        }
      ],
      "source": [
        "i = float(input(\" 請輸入年利率 = \"))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "X192Fbfe-VsG",
        "outputId": "ba29fb35-7d49-4800-97ae-ad758a1b2802"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            " 請輸入本金 = 10000\n"
          ]
        }
      ],
      "source": [
        "p = int(input(\" 請輸入本金 = \"))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Z5BzO0tf-VsG",
        "outputId": "7b529aa6-5ada-490a-edb2-13060570bfe0"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            " 請輸入存款年數 = 1\n"
          ]
        }
      ],
      "source": [
        "n = int(input(\" 請輸入存款年數 = \"))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "TBewjMfq-VsH",
        "outputId": "d7b533b9-6387-4d1e-db43-ad66f5034dab"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            " 本金加利息合計 = 10115.00\n"
          ]
        }
      ],
      "source": [
        "Principal_Interest =p * ((1 + i) ** n )\n",
        "print(\" 本金加利息合計 = %8.2f\" %(Principal_Interest))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gPdE1nlE-VsH"
      },
      "source": [
        "# 範例 3-29"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "jBBmmYjr-VsH",
        "outputId": "9ce67213-79e7-48cf-b1d4-33e47ad7b3cd"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "('Sun.', 'Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.')\n"
          ]
        }
      ],
      "source": [
        "List_Week = [\"Sun.\", \"Mon.\", \"Tue.\", \"Wed.\", \"Thu.\", \"Fri.\", \"Sat.\"]\n",
        "Tuple_FromList = tuple(List_Week)\n",
        "print(Tuple_FromList)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "822jIc7A-VsH",
        "outputId": "b304363a-588d-4027-bdb6-010d4ee9b77b"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "['Sun.', 'Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.']\n"
          ]
        }
      ],
      "source": [
        "List_FromTuple = list(Tuple_FromList)\n",
        "print(List_FromTuple)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "MyZqbEMU-VsH",
        "outputId": "ef61bf0b-333c-4d00-b056-b1c90da5b5c7"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'Fri.', 'Tue.', 'Sat.', 'Sun.', 'Wed.', 'Thu.', 'Mon.'}\n"
          ]
        }
      ],
      "source": [
        "Set_FromList = set(List_Week)\n",
        "print(Set_FromList)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "0V4Ivyzd-VsH",
        "outputId": "8dd98909-8615-4333-a43b-40755ecbaa72"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{0: 'Sun.', 1: 'Mon.', 2: 'Tue.', 3: 'Wed.', 4: 'Thu.', 5: 'Fri.', 6: 'Sat.'}\n"
          ]
        }
      ],
      "source": [
        "Enumerate_Data = enumerate(List_Week)\n",
        "print(dict(Enumerate_Data))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "iwcvmgTu-VsH"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8.5"
    },
    "colab": {
      "provenance": [],
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}