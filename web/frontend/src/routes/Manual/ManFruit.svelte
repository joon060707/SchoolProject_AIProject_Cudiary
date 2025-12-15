<script>
import Top from '../../lib/Top.svelte'
import MenuTitle from '../../lib/MenuTitle.svelte';

</script>


<Top />
<main>
  <MenuTitle title="🥒 Fruit Setting Stage" />

  <div class="manuals">
    <h3 class="center">Farming Manual</h3>
    <p>For more information, please refer to the following link:
      <a href="https://www.nongsaro.go.kr/portal/ps/psb/psbx/cropEbookLst.ps?menuId=PS65290&sText=&pageIndex=1&pageSize=10&sKeyword=&sNameOrderAt=Y&group2Cnt=&cropEbookGubunChk=&sStdPrdlstCode=&sStdTchnlgyCode=&stdPrdlstCode=&sRdaStdPrdlstCode=&sRdaStdTchnlgyCode=&kidofcomdtyNo=0&sOldDtShowAt=N&sSearchText=&sSearchType=srchType02&cNo=45&stdItemCd=VC010901&cropsEbookNm=%EC%98%A4%EC%9D%B4#" target="_blank" rel="noopener noreferrer">Cucurbits Cultivating Manual</a>
    </p>
    <div class="manual">
      <h4>PDF document</h4>
      <iframe src="src/assets/manual/man_fruit.pdf" title="example" frameborder="0"></iframe>
    </div>
      

  </div>
</main>


<style>
 
  p{
    margin-bottom: 0;
    margin-top: 10px;
  }
  .center{
    text-align: center;
  }
  .manuals{
    display: flex;
    flex-direction: column;
    align-items: center;
    min-width: 300px;
    max-width: 1000px;
    height: fit-content;
    margin: 20px auto;
    padding: 15px;
    border: 2px solid black;
    border-radius: 30px;
    background-color: rgba(240, 253, 255, 0.801);
    box-shadow: 0px 0px 10px rgb(0, 0, 0);
  }
  .manual{
    display: flex;
    flex-direction: column;
    margin: 10px 0;
    padding: 15px;
    border: 1px solid gray;
    border-radius: 20px;
    background-color: rgb(255, 255, 255);
    width: 100%;
    height: 1000px;
  }

  iframe {
    width: 100%;
    height: 100%;
    border: 2px solid rgb(0, 134, 0);
    border-radius: 20px;
    margin: 10px auto;
  }

</style>
