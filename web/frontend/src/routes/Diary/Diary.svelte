<script>
import DiaryTop from '../../lib/DiaryTop.svelte'
import Table from '../../lib/Table.svelte'
import MenuTitle from '../../lib/MenuTitle.svelte';
import logo_diary from '../../assets/diary.svg'
</script>


<DiaryTop />
<main>
  <MenuTitle title="Diary" icon={logo_diary} />
  <Table />
</main>


<style>

</style>
