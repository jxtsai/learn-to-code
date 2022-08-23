#CS50 week_5
- Date : Agust15th ~ August 28th
- https://cs50.harvard.edu/x/2022/weeks/5/
- 中文導讀

## 本週目標
- data structure in C
- pointers

## Content:  132 mins
### Data Structures



## 完成進度
請登入 https://ticktick.com

## my notes
### Date 2022-08-23


#### Structures syntax

今天的重點是回過頭從教科書來更清楚地認識 C 語言的自定資料結構 structure

CS50 課堂上提到的自定資料型態的語法是 

```
typedef struct
{
   int field_1_value;
   char field_2_value; 
   float  field_3_value;
}
structname;

```

用的關鍵字 keyword 是 typedef, struct，{} 裏頭是此資料類型的各欄位定義與名稱代號。例如 
int scores // 整數 scores
char name // 字符 name
甚至是放入自定的資料類型, 最常見的例子就是 linked lists 出現的 node
自定資料類型跟在}之後最後出現的是該資料的名稱。另一個寫法是:

```
struct structname
{
   int field_1_value;
   char field_2_value; 
   float  field_3_value;
    
};

```
第二種寫法的差異之處在於當宣告其資料類型時，得在前頭加上關鍵字 struct 與所命名的自定資料名稱，再加上此資料類型的新變數名稱，例如:

struct structname variablename // 一個structname 類型的變數名之為 variablenam 

第二種寫法的確是比較冗長

教科書上除了再次溫習 struct 語法，也討論了 struct 作為函數之參數，或是如何傳回 struct 的函數等等。如能對基本做到延伸應用，才算是對struct 真正掌握理解吧。


#### compound literals for structures

assign one or more values to a structure in single statement

variablename = (struct structname) { field_1_value, field_2_value, field_3_value, .....};


#### arrays of structures
C 語言的 structure 其作用是可以由用戶自行定義，把有關聯的資料透過 struct 集合使喚，而把 struct 儲存為陣列 array of structures ，例如:

// 第一種宣告自定 struct 變數的寫法，而此處 struct 變數亦為存有10個 struct(name) 之陣列,也就是這10個 struct element  其各帶有 struct 所賦予的"欄位"變數

structname variablename[10]

variablenam[0].field_1_value = somevalue;

// 第二種宣告 struct 變數的方式
struct structname variablename[10] 

#### structures containing structures


#### structures containing arrays

```
typedef struct
{
   int field_1_value[n];
   char field_2_value; 
   float  field_3_value;
}
structname;

```
struct 之欄位可以為陣列，不過似乎要在定義 struct 時,指明此 array 之元素數量 n 


## project

